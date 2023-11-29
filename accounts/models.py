from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

class CustomUser(AbstractUser):
    objects = UserManager()

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email