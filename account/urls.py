from django.urls import path
from .views import login_view, sign_up_view, logout_view, user_dashboard, create_fda_product_application, view_fda_product_application, create_business_cert_application, view_business_cert_application, user_applications, support_page, settings_page, edit_business_cert_application, edit_fda_product_application
from django.contrib.auth import views as auth_views

urlpatterns = [
    # User
    path('dashboard/', user_dashboard, name='user-dashboard'),
    path('fda_product_application/', create_fda_product_application, name='create-fda-product-application'),
    path('fda_product_application_details/<int:pk>/', view_fda_product_application, name='fda-product-application-details'),
    path('update_fda_product_application/<int:pk>/', edit_fda_product_application, name='edit-fda-product-application'),
    path('business_cert_application/', create_business_cert_application, name='create-business-cert-application'),
    path('business_cert_application_details/<int:pk>/', view_business_cert_application, name='business-cert-application-details'),
    path('update_business_certificate/<int:pk>/', edit_business_cert_application, name='edit-business-certificate-application'),
    path('my_applications/', user_applications, name='user-applications'),
    path('support/', support_page, name='support'),
    path('settings/', settings_page, name='settings'),

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
