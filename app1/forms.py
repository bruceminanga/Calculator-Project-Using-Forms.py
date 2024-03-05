from django import forms
from app1.models import Order

class OrderForm(forms.ModelForm):
    ACADEMIC_LEVEL_CHOICES = [
        ('undergraduate', 'Undergraduate'),
        ('high_school', 'High School'),
        ('masters', 'Masters'),
        ('phd', 'PhD'),
    ]

    SERVICE_TYPE_CHOICES = [
        ('writing', 'Writing'),
        ('editing', 'Editing'),
        ('proofreading', 'Proofreading'),
    ]

    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('GBP', 'GBP'),
    ]

    academic_level = forms.ChoiceField(choices=ACADEMIC_LEVEL_CHOICES)
    service_type = forms.ChoiceField(choices=SERVICE_TYPE_CHOICES)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)

    class Meta:
            model = Order  # replace with your model
            fields = ['academic_level', 'service_type', 'currency']  # replace with your fields


        

        