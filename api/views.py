from rest_framework import generics, serializers, permissions
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from .models import Employee, Product, Bill, Customer
from .serializers import EmployeeSerializer, EmployeePasswordSerializer, ProductSerializer, CustomerSerializer, BillSerializer, BillCreationSerializer

from django.db import models

# Employee views
class EmployeeListCreate(generics.ListCreateAPIView):
    """
    This view is used to create and retrieve the employee details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to retrieve, update and delete the employee details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

class EmployeePasswordUpdate(generics.UpdateAPIView):
    """
    This view is used to update the password of an employee without changing the other fields. This view is used by the employee to update their password without changing the other fields.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Employee.objects.all()
    serializer_class = EmployeePasswordSerializer
    lookup_field = 'pk'

    # The GET method will get the employee name and the POST method will update the password.
    def get(self, request, *args, **kwargs):
        employee = self.get_object()
        return Response({
            'aadhaar_card': employee.aadhaar_card,
            'name': employee.name
        })


# Product views
class ProductListCreate(generics.ListCreateAPIView):
    """
    This view is used to create and retrieve the product details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to retrieve, update and delete the product details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


# Customer views
class CustomerListCreate(generics.ListCreateAPIView):
    """
    This view is used to create and retrieve the customer details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to retrieve, update and delete the customer details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'


# Bill views
class BillListCreate(generics.ListCreateAPIView):
    """
    This view is used to create and retrieve the bill details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = Bill.objects.all()
    serializer_class = BillCreationSerializer

    def perform_create(self, serializer):
        """
        This method is used to calculate the total amount of the bill (including the discount) and deduct the stock of the product.
        """
        # Check if the product is in stock
        if serializer.validated_data['product'].stock < serializer.validated_data['quantity']:
            raise serializers.ValidationError('Product is out of stock')

        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        discount_percentage = serializer.validated_data['discount_percentage']
        total_amount = product.price * quantity * \
            (1 - discount_percentage / 100)
        serializer.save(total_amount=total_amount)

        # Deduct the stock of the product
        product.stock -= quantity
        product.save()


class BillRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is used to retrieve, update and delete the bill details.
    """
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    lookup_field = 'pk'


class Analytics(generics.GenericAPIView):
    """
    This view is used to generate analytics on the sales data.
    The following analytics are generated:
    1. Top 5 selling products by the REVENUE generated.
    2. The employee who has generated the most REVENUE.
    3. Top 5 selling products by the QUANTITY sold.
    4. The employee who has sold the most QUANTITY.
    """
    # class DummySerializer(serializers.Serializer):
    #     pass
    
    # JWT authentication
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        # Top 5 selling products by the revenue generated.
        # Explanation: values() method is used to group the data by the product and annotate() method is used to calculate the total amount for each product. The data is then ordered in descending order of total amount and the top 5 products are selected.
        top_5_revenue_generating_products = Bill.objects.values('product').annotate(
            total_amount=models.Sum('total_amount')).order_by('-total_amount')[:5]

        # The employee who has generated the most revenue.
        top_revenue_generating_employee = Bill.objects.values('sales_by').annotate(
            total_amount=models.Sum('total_amount')).order_by('-total_amount')[0]

        # Top 5 selling products by the quantity sold.
        top_5_sales_generating_products = Bill.objects.values('product').annotate(
            total_sales=models.Sum('quantity')).order_by('-total_sales')[:5]

        # The employee who has sold the most products.
        top_sales_generating_employee = Bill.objects.values('sales_by').annotate(
            total_sales=models.Sum('quantity')).order_by('-total_sales')[0]

        # Display names instead of IDs
        for item in top_5_revenue_generating_products:
            item['product'] = Product.objects.get(pk=item['product']).name

        top_revenue_generating_employee['sales_by'] = Employee.objects.get(
            pk=top_revenue_generating_employee['sales_by']).name

        for item in top_5_sales_generating_products:
            item['product'] = Product.objects.get(pk=item['product']).name

        top_sales_generating_employee['sales_by'] = Employee.objects.get(
            pk=top_sales_generating_employee['sales_by']).name

        return Response({
            'revenue': {
                'top_5_revenue_generating_products': top_5_revenue_generating_products,
                'top_revenue_generating_employee': top_revenue_generating_employee
            },
            'quantity': {
                'top_5_sales_generating_products': top_5_sales_generating_products,
                'top_sales_generating_employee': top_sales_generating_employee
            }
        })
