from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) # el email sea unico por usuario
    rut = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.username