from rest_framework import serializers
from .models import Employee, Product, Customer, Bill

class EmployeeSerializer(serializers.ModelSerializer):
    """
    This serializer is used to create, update and retrieve the employee details.
    - This serializer is to be used by the head of the company to create, update and retrieve the employee details.
    - The employee wishing to update their password can use the EmployeePasswordSerializer so that he/she can update the password without changing the other fields.
    """
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeePasswordSerializer(serializers.ModelSerializer):
    """
    This serializer is used to update the password of an employee without changing the other fields.
    """
    class Meta:
        model = Employee
        fields = ['password']

class ProductSerializer(serializers.ModelSerializer):
    """
    This serializer is used to create, update and retrieve the product details.
    """
    class Meta:
        model = Product
        fields = '__all__'
        
class CustomerSerializer(serializers.ModelSerializer):
    """
    This serializer is used to create, update and retrieve the customer details.
    """
    class Meta:
        model = Customer
        fields = '__all__'
        
class BillCreationSerializer(serializers.ModelSerializer):
    """
    This serializer is used to create a bill. The total amount and the date are calculated by the script and added to the database, hence they are excluded from the fields during creation.
    """
    class Meta:
        model = Bill
        exclude = ['total_amount']
        
    def to_representation(self, instance):
        """
        By default the response will contain the primary keys of the customer, product and sales_by fields. We are customizing the response to include the names of the customer, product and sales_by fields.
        """
        response = super().to_representation(instance)
        response['customer'] = instance.customer.name
        response['product'] = instance.product.name
        response['sales_by'] = instance.sales_by.name
        return response
    
class BillSerializer(serializers.ModelSerializer):
    """
    This serializer is used to retrieve the bill details. The customer name and product name are added to the response. The total amount and date are also included in the response.
    """
    class Meta:
        model = Bill
        fields = '__all__'
        
    def to_representation(self, instance):
        """
        By default the response will contain the primary keys of the customer, product and sales_by fields. We are customizing the response to include the names of the customer, product and sales_by fields.
        """
        response = super().to_representation(instance)
        response['customer'] = instance.customer.name
        response['product'] = instance.product.name
        response['sales_by'] = instance.sales_by.name
        
        return response