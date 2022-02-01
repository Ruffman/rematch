from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from polymorphic.models import PolymorphicModel

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
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class County(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.state.__str__() + "::" + self.name


class Object_Address(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    county = models.ForeignKey(County, on_delete=models.PROTECT)
    zip_code = models.IntegerField(default=00000)
    city_name = models.TextField(default="Default City")
    street_name = models.TextField(default="Default Street Name")
    street_number = models.IntegerField(default=000)

    def __str__(self):
        return (
            self.county.__str__()
            + "::"
            + str(self.zip_code)
            + "::"
            + self.city_name
            + "::"
            + self.street_name
            + "::"
            + str(self.street_number)
        )


class Object_Location_Detail(models.Model):
    is_sunny = models.BooleanField(default=False, blank=True)
    is_calm = models.BooleanField(default=False, blank=True)
    at_hillside = models.BooleanField(default=False, blank=True)
    near_public_transport = models.BooleanField(default=False, blank=True)
    near_freeway = models.BooleanField(default=False, blank=True)
    near_stores = models.BooleanField(default=False, blank=True)
    near_recreation = models.BooleanField(default=False, blank=True)
    near_education = models.BooleanField(default=False, blank=True)
    has_nice_view = models.BooleanField(default=False, blank=True)

    # def __str__(self):
    #     return self.name


class Recreation_Area_Types(models.Model):
    has_balcony = models.BooleanField(default=False, blank=True)
    has_roof_terrace = models.BooleanField(default=False, blank=True)
    has_terrace = models.BooleanField(default=False, blank=True)
    has_garden = models.BooleanField(default=False, blank=True)
    has_winter_garden = models.BooleanField(default=False, blank=True)
    has_loggia = models.BooleanField(default=False, blank=True)
    something_different = models.TextField(blank=True)

    # def __str__(self):
    #     return self.name


class Facility_Types(models.Model):
    has_storeroom = models.BooleanField(default=False, blank=True)
    has_carport = models.BooleanField(default=False, blank=True)
    has_fitted_kitchen = models.BooleanField(default=False, blank=True)
    has_elevator = models.BooleanField(default=False, blank=True)
    has_garage = models.BooleanField(default=False, blank=True)
    has_cellar = models.BooleanField(default=False, blank=True)
    has_parking_area = models.BooleanField(default=False, blank=True)
    is_furnished = models.BooleanField(default=False, blank=True)
    is_barrier_free = models.BooleanField(default=False, blank=True)
    is_partially_furnished = models.BooleanField(default=False, blank=True)

    # def __str__(self):
    #     return self.name


class Heating_Type(models.Model):
    type_name = models.CharField(max_length=16)

    def __str__(self):
        return self.type_name


class Object(PolymorphicModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    object_type = models.ForeignKey(
        Object_Type,
        verbose_name="Objektart",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    finance_type = models.ForeignKey(
        Finance_Type,
        verbose_name="Wohnart",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    object_address = models.ForeignKey(
        Object_Address,
        verbose_name="Objektadresse",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    title = models.TextField(default="Default Title", verbose_name="Titel")
    short_description = models.TextField(
        default="Default Short Description", verbose_name="Kurzbeschreibung"
    )

    # ideal customer idea / ideal object propertys
    number_adults = models.IntegerField(null=True, blank=True)
    number_couples = models.IntegerField(null=True, blank=True)
    number_children = models.IntegerField(null=True, blank=True)

    pets_number = models.IntegerField(null=True, blank=True)
    pets_are_allowed = models.BooleanField(blank=True)

    number_cars = models.IntegerField(null=True, blank=True)

    number_homeoffice = models.IntegerField(null=True, blank=True)
    number_kitchens = models.IntegerField(null=True, blank=True)
    number_bathrooms = models.IntegerField(null=True, blank=True)
    number_bedrooms = models.IntegerField(null=True, blank=True)

    living_area = models.IntegerField(null=True, blank=True)

    # object location properties
    location_details = models.OneToOneField(
        Object_Location_Detail, on_delete=models.PROTECT
    )

    # recreational area
    recreational_area_detail = models.OneToOneField(
        Recreation_Area_Types, on_delete=models.PROTECT
    )

    # facilities
    facilities_detail = models.OneToOneField(Facility_Types, on_delete=models.PROTECT)

    # heating type
    heating_type = models.ForeignKey(Heating_Type, on_delete=models.PROTECT)

    # object building properties
    is_modern = models.BooleanField(default=False, blank=True)
    is_built_sustainable = models.BooleanField(default=False, blank=True)

    # availability
    is_available_now = models.BooleanField(default=False, blank=True)
    available_at_date = models.DateField(null=True, blank=True)

    # if object is Apartment or Room
    living_floor = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return (
            self.object_type.__str__()
            + "::"
            + self.finance_type.__str__()
            + "::"
            + self.object_address.__str__()
            + "::"
            + self.title
            + "::"
            + self.user.__str__()
        )

    def save(self, *args, **kwargs):
        super().save(args, **kwargs)


class Offer(Object):
    monthly_rent_cold = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=9
    )
    monthly_incidentals_price = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=9
    )  # TODO model für NBK
    buy_price = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=17
    )
    security_deposit = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=17
    )

    class Meta:
        verbose_name = "Offer"

    def __str__(self):
        return super().__str__()


class Request(Object):
    monthly_income = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=9
    )
    available_cash = models.DecimalField(
        null=True, blank=True, decimal_places=2, max_digits=17
    )

    class Meta:
        verbose_name = "Request"

    def __str__(self):
        return super().__str__()


class Object_Image(models.Model):
    related_offer = models.ForeignKey(Offer, on_delete=models.CASCADE, null=True)
    related_request = models.ForeignKey(Request, on_delete=models.CASCADE, null=True)

    image = models.ImageField()

    def __str__(self):
        if related_offer:
            return "OfferID::" + str(self.related_offer.id)
        if related_request:
            return "RequestID::" + str(self.related_request.id)


class Important_Address(Object_Address):
    related_offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, null=True
    )  # TODO: find out why naming it only offer clashes with object_address field named offer
    related_request = models.ForeignKey(
        Request, on_delete=models.CASCADE, null=True
    )  # TODO: find out why naming it only request clashes with object_address field named request

    def __str__(self):
        if related_offer:
            return "OfferID::" + str(self.related_offer.id)
        if related_request:
            return "RequestID::" + str(self.related_request.id)
