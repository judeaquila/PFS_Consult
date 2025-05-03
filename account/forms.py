from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, FDAApplication, BusinessCertificateApplication

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name',]

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email')


# FDA Application Forms
class FDAApplicationForm(forms.ModelForm):
    class Meta:
        model = FDAApplication
        fields = [
            'business_certificate', 'business_name', 'location', 'products', 'logo', 'lab_results', 'product_labels', 'food_handler_cert', 'process_description', 'voice_note', 'facility_video', 'items_equipment', 'staff_roles',
        ]

        widgets = {
            'products': forms.Textarea(attrs={'rows': 3}),
            'process_description': forms.Textarea(attrs={'rows': 3}),
            'items_equipment': forms.Textarea(attrs={'rows': 3}),
            'staff_roles': forms.Textarea(attrs={'rows': 3}),
        }


# Business Certificate Forms
class BusinessCertificateForm(forms.ModelForm):
    class Meta:
        model = BusinessCertificateApplication
        fields = [
            'company_name', 'nature_of_business', 'postal_address', 'contact_number_one', 'contact_number_two', 'company_email', 'company_building_number', 'company_landmark', 'area', 'district', 'company_gps_address', 'ghana_card_number', 'tin_number',
        ]

        widgets = {
            'postal_address': forms.Textarea(attrs={'rows': 3}),
        }