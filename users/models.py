from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('LIB', 'Librarian'),
        ('PAT', 'Patron'),
    ]
    name = models.CharField(max_length=100, null=True)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)
    email = models.EmailField(null=True)
    membership_id = models.CharField(max_length=20, default='')  # Add membership ID field

    def __str__(self):
        return self.username



