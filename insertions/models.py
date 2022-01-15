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
    object_type = models.ForeignKey(Object_Type, verbose_name='object type', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=127)
    short_description = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    city_name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    street_number = models.IntegerField()
    living_area = models.IntegerField()
    monthly_rent_price = models.DecimalField(decimal_places=2, max_digits=9)
    buy_price = models.DecimalField(decimal_places=2, max_digits=17)

    class Meta:
        abstract = True

    def __str__(self):
        return (str(self.object_type) + '::' + str(self.zip_code) + '::' + self.city_name + '::'
                + self.street_name + '::' + str(self.street_number))

    def save(self, *args, **kwargs):
        super().save(args, **kwargs)


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
    user = models.OneToOneField(User, verbose_name='offer', on_delete=models.CASCADE)
    object = models.OneToOneField(Object, verbose_name='object', on_delete=models.CASCADE) # # TODO: model so that object can be any child model inheriting from object

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(args, **kwargs)

    class Meta:
        unique_together = ['user', 'object']



class Request(models.Model):
    user = models.OneToOneField(User, verbose_name='request', on_delete=models.CASCADE)
    object = models.OneToOneField(Object, verbose_name='object', on_delete=models.CASCADE) # # TODO: model so that object can be any child model inheriting from object

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ['user', 'object']
