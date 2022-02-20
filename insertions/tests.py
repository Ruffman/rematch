from django.test import TestCase

from accounts.models import User
from .models import Offer, Request, Object_Type, Finance_Type, Heating_Type

# Create your tests here.
class TestCreateOffer(TestCase):
    def setUp(self):
        self.testUserName = "test1"
        self.testUserEmail = "test@test.com"
        self.testUserPass = "123test123"
        User.objects.create(
            username=self.testUserName,
            email=self.testUserEmail,
            password=self.testUserPass,
        )

        self.testObjectType = Object_Type.objects.create(type_name="Haus")
        self.testFinanceType = Object_Type.objects.create(type_name="Kaufen")
        self.testHeatingType = Object_Type.objects.create(type_name="Gas")

        self.testTitle = "Hier, ein neues Haus"
        self.testShortDescription = "Es ist sehr schön"

        # self.testCreatedAt = models.DateTimeField(auto_now_add=True)
        # self.testLastUpdated = models.DateTimeField(auto_now=True)
        # self.testAvailableAtDate

        self.testNumberAdults = 2
        self.testNumberCouples = 1
        self.testNumberChildren = 3
        self.testPetsNumber = 2
        self.testPetsAreAllowed = True
        self.testNumberCars = 2
        self.testNumberHomeoffice = 1
        self.testNumberKitchens = 1
        self.testNumberBathrooms = 2
        self.testNumberBedrooms = 4
        self.testLivingArea = 130
        self.testIsModern = True
        self.testIsBuiltSustainable = False
        self.testIsAvailableNow = True
        self.testLivingFloor = 1

        Offer.objects.create(
            user=User.objects.first(),
            object_type=self.testObjectType,
            finance_type=self.testFinanceType,
            heating_type=self.testHeatingType,
            title=self.testTitle,
            short_description=self.testShortDescription,
            number_adults=self.testNumberAdults,
            number_couples=self.testNumberCouples,
            number_childern=self.testNumberChildren,
            pets_number=self.testPetsNumber,
            pets_are_allowed=self.testPetsAreAllowed,
            number_cars=self.testNumberCars,
            number_homeoffice=self.testNumberHomeoffice,
            number_kitchens=self.testNumberKitchens,
            number_bathrooms=self.testNumberBathrooms,
            number_bedrooms=self.testNumberBedrooms,
            living_area=self.testLivingArea,
            is_modern=self.testIsModern,
            is_built_sustainable=self.testIsBuiltSustainable,
            is_available_now=self.testIsAvailableNow,
            living_floor=self.testLivingFloor,
        )

        def test_exists_offer(self):
            self.assertEqual(Offer.objects.count(), 1)
            self.Offer = Offer.objects.first()
            self.User = User.objects.first()
            self.assertEqual(self.Offer.users, self.User)
            self.assertEqual(self.Offer.object_type, self.testObjectType)
            self.assertEqual(self.Offer.finance_type, self.testFinanceType)
            self.assertEqual(self.Offer.heating_type, self.testHeatingType)
            self.assertEqual(self.Offer.title, self.testTitle)
            self.assertEqual(self.Offer.short_description, self.testShortDescription)
            self.assertEqual(self.Offer.number_adults, self.testNumberAdults)
            self.assertEqual(self.Offer.number_couples, self.testNumberCouples)
            self.assertEqual(self.Offer.number_childern, self.testNumberChildren)
            self.assertEqual(self.Offer.pets_number, self.testPetsNumber)
            self.assertEqual(self.Offer.pets_are_allowed, self.testPetsAreAllowed)
            self.assertEqual(self.Offer.number_cars, self.testNumberCars)
            self.assertEqual(self.Offer.number_homeoffice, self.testNumberHomeoffice)
            self.assertEqual(self.Offer.number_kitchens, self.testNumberKitchens)
            self.assertEqual(self.Offer.number_bathrooms, self.testNumberBathrooms)
            self.assertEqual(self.Offer.number_bedrooms, self.testNumberBedrooms)
            self.assertEqual(self.Offer.living_area, self.testLivingArea)
            self.assertEqual(self.Offer.is_modern, self.testIsModern)
            self.assertEqual(self.Offer.is_built_sustainable, self.testIsBuiltSustainable)
            self.assertEqual(self.Offer.is_available_now, self.testIsAvailableNow)
            self.assertEqual(self.Offer.living_floor, self.testLivingFloor)
