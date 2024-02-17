from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name_one', 'name_two', 'location_one', 'location_two', 'status']
