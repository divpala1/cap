from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Employee(models.Model):
    aadhaar_card = models.CharField(max_length=12, unique=True, verbose_name='Aadhaar Card Number')
    name = models.CharField(max_length=255, verbose_name='Employee Name')
    salary = models.FloatField(verbose_name='Salary')
    password = models.CharField(max_length=255, verbose_name='Password', default='password@123')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product Name')
    price = models.FloatField(verbose_name='Price')
    stock = models.IntegerField(verbose_name='Stock', default=0)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name='Customer Name')
    email = models.EmailField(verbose_name='Email Address', unique=True, null=False, blank=False)
    phone = models.CharField(max_length=10, unique=True, null=False, blank=False, verbose_name='Phone Number')
    
    def __str__(self):
        return self.name
    
class Bill(models.Model):
    methods = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('UPI', 'UPI')
    )
    discount_range = (0.0, 100.0)
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer Name')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product Name')
    quantity = models.IntegerField(verbose_name='Quantity Purchased', validators=[MinValueValidator(1)])
    discount_percentage = models.FloatField(verbose_name='Discount Percentage', validators=[MinValueValidator(discount_range[0]), MaxValueValidator(discount_range[1])])
    method = models.CharField(max_length=5, choices=methods, default='Cash', verbose_name='Payment Method')
    sales_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, verbose_name='Sales Person')
    
    # Following fields are automatically filled by the system
    date = models.DateTimeField(auto_now_add=True, verbose_name='Date and Time of Purchase')
    total_amount = models.FloatField(verbose_name='Total Amount')
    
    def __str__(self):
        return str(self.date) + '-' + self.customer.name
