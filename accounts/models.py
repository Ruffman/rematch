from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



# Create your models here.
class User(AbstractUser):
    title = models.CharField(max_length=10)
    bio = models.TextField(max_length=1000, blank=True)
    city_name = models.CharField(max_length=63, blank=True)
    zip_code = models.IntegerField(null=True)
    birth_date = models.DateField(default=0, blank=True)
