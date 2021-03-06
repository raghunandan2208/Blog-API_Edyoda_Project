from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile/', blank=True)
    is_author = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email']
