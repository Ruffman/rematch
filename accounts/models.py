from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



# Create your models here.
class Title_Type(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name



class Academic_Title_Type(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name



class Vocation_Type(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name



class User(AbstractUser):
    title = models.ForeignKey(Title_Type, verbose_name='Anrede', on_delete=models.PROTECT, null=True, blank=True)
    academic_title = models.ForeignKey(Academic_Title_Type, verbose_name='Titel', on_delete=models.PROTECT, null=True, blank=True)
    voaction = models.ForeignKey(Vocation_Type, verbose_name='Berufsgruppe', on_delete=models.PROTECT, null=True, blank=True)

    bio = models.TextField(max_length=1000, blank=True)
    city_name = models.CharField(max_length=63, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
