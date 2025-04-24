from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, FDAApplication

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