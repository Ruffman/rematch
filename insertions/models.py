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



class Finance_Type(models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name



class State(models.Model):
    name = models.CharField(max_length=31)

    def __str__(self):
        return self.name



class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.state.__str__() + '::' + self.name



class Object_Address(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    county = models.ForeignKey(County, on_delete=models.PROTECT)
    zip_code = models.IntegerField(default=00000)
    city_name = models.CharField(max_length=255, default='Default City')
    street_name = models.CharField(max_length=255, default='Default Street Name')
    street_number = models.IntegerField(default=000)

    def __str__(self):
        return (self.county.__str__() + '::' + str(self.zip_code) + '::' + self.city_name + '::' + self.street_name + '::' + str(self.street_number))



class Object(PolymorphicModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    object_type = models.ForeignKey(Object_Type, verbose_name='Objektart', on_delete=models.PROTECT, null=True, blank=True)
    finance_type = models.ForeignKey(Finance_Type, verbose_name='Wohnart', on_delete=models.PROTECT, null=True, blank=True)
    object_address = models.ForeignKey(Object_Address, verbose_name='Objektadresse', on_delete=models.PROTECT, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=127, default='Default Title', verbose_name='Titel')
    short_description = models.CharField(max_length=255, default='Default Short Description', verbose_name='Kurzbeschreibung')

    # ideal customer idea / ideal object propertys
    number_adults = models.IntegerField(null=True, blank=True)
    number_couples = models.IntegerField(null=True, blank=True)
    number_children = models.IntegerField(null=True, blank=True)

    number_pets = models.IntegerField(null=True, blank=True)
    number_cars = models.IntegerField(null=True, blank=True)

    number_homeoffice = models.IntegerField(null=True, blank=True)
    number_kitchens = models.IntegerField(null=True, blank=True)
    number_bathrooms = models.IntegerField(null=True, blank=True)
    number_bedrooms = models.IntegerField(null=True, blank=True)

    living_area = models.IntegerField(null=True, blank=True)

    # object location properties
    location_is_sunny = models.BooleanField(default=False, blank=True)
    location_is_calm = models.BooleanField(default=False, blank=True)
    location_at_hillside = models.BooleanField(default=False, blank=True)
    location_near_public_transport = models.BooleanField(default=False, blank=True)
    location_near_freeway = models.BooleanField(default=False, blank=True)
    location_near_stores = models.BooleanField(default=False, blank=True)
    location_near_recreation = models.BooleanField(default=False, blank=True)
    location_near_education = models.BooleanField(default=False, blank=True)
    location_has_nice_view = models.BooleanField(default=False, blank=True)

    # object building properties
    is_modern = models.BooleanField(default=False, blank=True)
    is_built_sustainable = models.BooleanField(default=False, blank=True)

    # availability
    is_available_now = models.BooleanField(default=False, blank=True)
    available_at_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return (self.object_type.__str__() + '::' + self.finance_type.__str__() + '::'
                + self.object_address.__str__() + '::' + self.title + '::' + self.user.__str__()
)

    def save(self, *args, **kwargs):
        super().save(args, **kwargs)



class Offer(Object):
    monthly_rent_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=9)
    buy_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=17)

    class Meta:
        verbose_name = 'Offer'

    def __str__(self):
        return super().__str__()


class Request(Object):
    monthly_income = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=9)
    available_cash = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=17)

    class Meta:
        verbose_name = 'Request'

    def __str__(self):
        return super().__str__()



class Object_Image(models.Model):
    related_offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    related_request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True)

    image = models.ImageField()

    def __str__(self):
        if(related_offer):
            return 'OfferID::' + str(self.related_offer.id)
        if(related_request):
            return 'RequestID::' + str(self.related_request.id)



class Important_Address(Object_Address):
    related_offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True) # TODO: find out why naming it only offer clashes with object_address field named offer
    related_request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True) # TODO: find out why naming it only request clashes with object_address field named request

    def __str__(self):
        if(related_offer):
            return 'OfferID::' + str(self.related_offer.id)
        if(related_request):
            return 'RequestID::' + str(self.related_request.id)
