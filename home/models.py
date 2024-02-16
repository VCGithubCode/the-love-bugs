from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    STATUS_CHOICES = [
        ('option1', 'Situationship'),
        ('option2', 'Officially together'),
        ('option3', 'Engaged'),
        ('option4', 'Married'),
    ]
    
    name_one = models.CharField(max_length=30, blank=True, null=True)
    name_two = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)
