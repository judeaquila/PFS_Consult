from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FDAApplication, BusinessCertificateApplication, UserActivity
from .forms import CustomUserCreationForm, CustomUserUpdateForm

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserUpdateForm

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FDAApplication)
admin.site.register(BusinessCertificateApplication)
admin.site.register(UserActivity)