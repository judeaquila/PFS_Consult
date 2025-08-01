from django import forms
from .models import ProductIntake

class ProductIntakeForm(forms.ModelForm):
    class Meta:
        model = ProductIntake
        fields = '__all__'
        exclude = ['user', 'custom_id', 'payment_status', 'application_status', 'submitted_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['goals'] = forms.MultipleChoiceField(choices=ProductIntake.GOALS_CHOICES, widget=forms.CheckboxSelectMultiple, label='What is/are your goal(s) for the Product?')
        self.fields['target_market'] = forms.MultipleChoiceField(choices=ProductIntake.TARGET_MARKET_CHOICES, widget=forms.CheckboxSelectMultiple, label='What is your Target Market?')
        self.fields['packaging_style'] = forms.MultipleChoiceField(choices=ProductIntake.PACKAGING_CHOICES, widget=forms.CheckboxSelectMultiple, label='What Packaging Style are you envisioning?')
        self.fields['expected_launch_date'].widget = forms.DateInput(attrs={'type':'date'})
