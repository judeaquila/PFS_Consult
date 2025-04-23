from django.urls import path
from .views import home, fda_services, other_services, login_redirect

urlpatterns = [
    path('', home, name='home'),
    path('fda_services/', fda_services, name='fda-services'),
    path('other_services/', other_services, name='other-services'),
    path('redirecting_to_login/', login_redirect, name='login-redirect'),
]