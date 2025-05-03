from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, FDAApplication, BusinessCertificateApplication
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FDAApplication)
admin.site.register(BusinessCertificateApplication)