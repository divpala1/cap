from django.contrib import admin
from .models import Employee, Product, Bill, Customer

admin.site.register(Employee)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(Customer)