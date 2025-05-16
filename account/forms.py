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
            'full_name', 'dob', 'marital_status', 'place_of_birth', 'nationality', 'occupation', 'contact_number_one', 'contact_number_two', 'email', 'business_name', 'nature_of_business', 'type_of_business', 'postal_address', 'company_email', 'company_building_number', 'company_landmark', 'area', 'district', 'company_gps_address', 'ghana_card_number', 'tin_number',
        ]

        widgets = {
            'postal_address': forms.Textarea(attrs={'rows': 3}),
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        labels = {
            'full_name': 'Full Name',
            'dob': 'Date of Birth',
            'marital_status': 'Marital Status',
            'place_of_birth': 'Place of Birth',
            'nationality': 'Nationality',
            'occupation': 'Occupation',
            'contact_number_one': 'Phone Number 1',
            'contact_number_two': 'Phone Number 2',
            'email': 'Email',
            'business_name': 'Name of Business',
            'nature_of_business': 'Nature of Business',
            'type_of_business': 'Type of Business',
            'postal_address': 'Postal Address',
            'company_email': 'Email of Business',
            'company_building_number': 'Business Building Number',
            'company_landmark': 'Landmark',
            'area': 'Area of Business (Location)',
            'district': 'District of Business',
            'company_gps_address': 'Business GPS Address',
            'ghana_card_number': 'Ghana Card Number',
            'tin_number': 'Tax Identification Number (TIN)',
        }