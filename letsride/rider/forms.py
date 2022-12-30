from django import forms
from .models import Rider


class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ['name', 'start_location', 'end_location' ,'phone_number']
