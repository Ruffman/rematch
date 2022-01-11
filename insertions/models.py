from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils import timezone


from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.

class Object_Type(models.Model):
    type_name = models.CharField(max_length=20)

    def __str__(self):
        return self.type_name



class Object(models.Model):
    object_type = models.ForeignKey(Object_Type, verbose_name='object type', on_delete=models.PROTECT) # TODO: do i need this here as well to reference the right object table?
    created_at = models.DateTimeField(timezone.now())
    zip_code = models.IntegerField()
    street_name = models.CharField(max_length=150)
    street_number = models.IntegerField()
    living_area = models.IntegerField()
    monthly_rent_price = models.DecimalField(decimal_places=2, max_digits=9)
    buy_price = models.DecimalField(decimal_places=2, max_digits=9)


# class Property(Object):
#
#
# class House(Object):
#
#
# class Apartment(Object):
#

# class Room(Object):
#     num_other_tennants = models.IntegerField()


class Offer(models.Model):
    user = models.ForeignKey(User, verbose_name='offer', on_delete=models.CASCADE)
    object = models.ForeignKey(Object, verbose_name='object id', on_delete=models.CASCADE) # # TODO: model so that object can be any child model inheriting from object

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ['user', 'object']



class Request(models.Model):
    user = models.ForeignKey(User, verbose_name='request', on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username
