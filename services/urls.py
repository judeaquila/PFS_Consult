from django.urls import path
from .views import product_development

urlpatterns = [
    path('product-development/', product_development, name='product_development'),
]
