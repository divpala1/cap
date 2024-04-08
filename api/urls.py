from django.urls import path
from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView

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
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # DRF Spectacular URLs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI:
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI:
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

"""
JWT Explained:
The endpoint `/token/get/` allows you to post a valid username and password to obtain a pair of tokens:
- Access token
- Refresh token

Once having the access token, you can add it to the header of an HTTP request to call other APIs. When the access token is expired, you can call the `token/refresh/` API endpoint to get the new access token.
"""