from django import forms
from .models import ProductIntake

class ProductIntakeForm(forms.ModelForm):
    class Meta:
        model = ProductIntake
        fields = '__all__'
        widgets = {
            'goals': forms.CheckboxSelectMultiple(choices=ProductIntake.GOALS_CHOICES),
            'target_market': forms.CheckboxSelectMultiple(choices=ProductIntake.TARGET_MARKET_CHOICES),
            'packaging_style': forms.CheckboxSelectMultiple(choices=ProductIntake.PACKAGING_CHOICES),
            'expected_launch_date': forms.DateInput(attrs={'type': 'date'}),
            'ingredient_or_dietary_notes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        goals = cleaned_data.get('goals', [])
        other_goal = cleaned_data.get('other_goal')
        target_market = cleaned_data.get('target_market', [])
        other_target_market = cleaned_data.get('other_target_market')
        packaging_style = cleaned_data.get('packaging_style', [])
        custom_packaging = cleaned_data.get('custom_packaging')

        if 'other' in goals and not other_goal:
            self.add_error('other_goal', 'Please specify your "Other" goal.')

        if 'other' in target_market and not other_target_market:
            self.add_error('other_target_market', 'Please specify your "Other" target market.')

        if 'custom' in packaging_style and not custom_packaging:
            self.add_error('custom_packaging', 'Please describe the custom packaging.')