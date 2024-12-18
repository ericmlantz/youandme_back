from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstractUser is a class provided by Django that serves as a base class for creating custom user models.
# It is part of Django’s built-in authentication framework and includes all the fields and methods required 
# for managing users in a Django application: username, password, email, first_name, last_name, 
# authentication-related fields, and permissions/groups

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)