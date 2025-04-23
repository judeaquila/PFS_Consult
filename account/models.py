from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50, blank=True, null=True)
    # company_name = models.CharField(max_length=250, blank=True, null=True)
    # phone_number = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email