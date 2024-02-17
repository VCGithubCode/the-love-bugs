from django import forms
from .models import Profile
from django.forms.fields import DateTimeField


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name_one', 'name_two', 'location_one', 'location_two', 'status', 'datetime_field']
        widgets = {
            'datetime_field': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

