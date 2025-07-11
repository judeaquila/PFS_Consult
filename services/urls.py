from django.urls import path
from .views import pd_home, product_development, pd_thank_you, product_development_details, product_development_delete, product_development_update

urlpatterns = [
    path('product-development/', pd_home, name='pd_home'),
    path('product-development/application', product_development, name='product_development'),
    path('product-development/application-success/<int:pk>/', pd_thank_you, name='pd_thank_you'),
    path('product-development/details/<int:pk>/', product_development_details, name='product_development_details'),
    path('product-development/delete/<int:pk>/', product_development_delete, name='pd_delete'),
    path('product-development/update/<int:pk>/', product_development_update, name='pd_update'),
]
