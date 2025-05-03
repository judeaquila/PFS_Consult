from django.urls import path
from .views import login_view, sign_up_view, logout_view, user_dashboard, create_fda_application, view_fda_application, create_business_cert_application, view_business_cert_application
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', user_dashboard, name='user-dashboard'),
    path('fda_application/', create_fda_application, name='create-fda-application'),
    path('fda_application_details/<int:pk>/', view_fda_application, name='fda-application-details'),
    path('business_cert_application/', create_business_cert_application, name='create-business-cert-application'),
    path('business_cert_application_details/<int:pk>/', view_business_cert_application, name='business-cert-application-details'),

    # Auth Paths
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign_up/', sign_up_view, name='sign_up'),

    # Built-in Auth Functionalities
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
