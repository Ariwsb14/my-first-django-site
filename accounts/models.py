from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100 , unique=True)
# Create your models here.
