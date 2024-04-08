from django.urls import path
from . import views

# Python code for making requests to the API from another Python application
"""
======================================================================
Demo request for adding an employee to the database from another Python application:
======================================================================
import requests
import json

url = 'http://localhost:8000/api/employees/'

data = {
    'name': 'John Doe',
    'emp_id': 101,
    'salary': 50000
}

response = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print(response.status_code)

======================================================================
Demo request for updating an employee in the database from another Python application:
======================================================================
import requests
import json

url = 'http://localhost:8000/api/employees/101/'

data = {
    'name': 'John Doe',
    'emp_id': 101,
    'salary': 60000
}

response = requests.put(url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
print(response.status_code)

======================================================================
Demo request for deleting an employee from the database from another Python application:
======================================================================
import requests
import json

url = 'http://localhost:8000/api/employees/101/'

response = requests.delete(url)
print(response.status_code)
"""

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Employees API
    path('employees/', views.EmployeeListCreate.as_view(), name='employee-view-create'),
    path('employees/<int:pk>/', views.EmployeeRetrieveUpdateDestroy.as_view(), name='employee-view-update-delete'),
    path('employees/<int:pk>/password/', views.EmployeePasswordUpdate.as_view(), name='employee-password-update'),
    
    # Customers API
    path('customers/', views.CustomerListCreate.as_view(), name='customer-view-create'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customer-view-update-delete'),
    
    # Products API
    path('products/', views.ProductListCreate.as_view(), name='product-view-create'),
    path('products/<int:pk>/', views.ProductRetrieveUpdateDestroy.as_view(), name='product-view-update-delete'),
    
    # Bills API
    path('bills/', views.BillListCreate.as_view(), name='bill-view-create'),
    path('bills/<int:pk>/', views.BillRetrieveUpdateDestroy.as_view(), name='bill-view-update-delete'),
    
    # Analytics API
    path('analytics/', views.Analytics.as_view(), name='analytics-view'),
    
    # jwt
    path('token/get/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

"""
JWT Explained:
The endpoint `/token/get/` allows you to post a valid username and password to obtain a pair of tokens:
- Access token
- Refresh token

Once having the access token, you can add it to the header of an HTTP request to call other APIs. When the access token is expired, you can call the `token/refresh/` API endpoint to get the new access token.
"""