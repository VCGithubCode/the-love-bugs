from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    name_one = forms.CharField(max_length=30, label='Name One')
    name_two = forms.CharField(max_length=30, label='Name Two')
    # position_one
    # position_two
    STATUS_CHOICES = [
        ('option1', 'Situationship'),
        ('option2', 'Officially together'),
        ('option3', 'Engaged'),
        ('option4', 'Married'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Status', widget=forms.Select)
    # sum_time_together
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.name_one = self.cleaned_data['name_one']
        user.name_two = self.cleaned_data['name_two']
        user.status = self.cleaned_data['status']
        user.save()
        return user