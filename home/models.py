from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    STATUS_CHOICES = [
        ('option1', 'Situationship'),
        ('option2', 'Officially together'),
        ('option3', 'Engaged'),
        ('option4', 'Married'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name_one = models.CharField(max_length=30, blank=True, null=True)
    name_two = models.CharField(max_length=30, blank=True, null=True)
    location_one = models.CharField(max_length=100, blank=True)
    location_two = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)
    datetime_field = models.DateTimeField(blank=True, null=True)
    # picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)