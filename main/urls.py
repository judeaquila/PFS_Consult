from django.urls import path
from .views import home, fda_services, other_services, login_redirect, admin_dashboard, admin_business_cert_application_details, admin_fda_product_application_details, edit_admin_business_cert_application_details, edit_admin_fda_product_application_details, change_business_cert_application_status, change_fda_product_application_status, manage_users, add_user, edit_user, delete_user, toggle_user_active

urlpatterns = [
    path('', home, name='home'),
    path('fda_services/', fda_services, name='fda-services'),
    path('other_services/', other_services, name='other-services'),
    path('redirecting_to_login/', login_redirect, name='login-redirect'),

    # Admin
    path('dashboard/admin/', admin_dashboard, name='admin-dashboard'),
    path('dashboard/admin/business_cert_application_details/<int:pk>/', admin_business_cert_application_details, name='admin-business-cert-application-details'),
    path('dashboard/admin/fda_product_application_details/<int:pk>/', admin_fda_product_application_details, name='admin-fda-product-application-details'),
    path('dashboard/admin/edit_business_cert_application_details/<int:pk>/', edit_admin_business_cert_application_details, name='admin-edit-business-cert-application-details'),
    path('dashboard/admin/edit_fda_product_application_details/<int:pk>/', edit_admin_fda_product_application_details, name='admin-edit-fda-product-application-details'),
    path('dashboard/admin/change_business_cert_application_status/<int:pk>/change_status/<str:new_status>/', change_business_cert_application_status, name='admin-change-business-cert-application-status'),
    path('dashboard/admin/change_fda_product_application_status/<int:pk>/change_status/<str:new_status>/', change_fda_product_application_status, name='admin-change-fda-product-application-status'),
    path('dashboard/admin/users/manage', manage_users, name='manage-users'),
    path('dashboard/admin/users/add/', add_user, name='add-user'),
    path('dashboard/admin/users/<int:pk>/edit/', edit_user, name='edit-user'),
    path('dashboard/admin/users/<int:pk>/delete/', delete_user, name='delete-user'),
    path('dashboard/admin/users/<int:pk>/toggle-active/', toggle_user_active, name='toggle-user-active'),
]