from .models import Offer, Request, Object_Type, Finance_Type, Heating_Type
from accounts.models import User

import random


def create_offer(request):
    objectTypeList = Object_Type.objects.all()
    financeTypeList = Finance_Type.objects.all()
    heatingTypeList = Heating_Type.objects.all()

    objectType = random.choice(objectTypeList)
    financeType = random.choice(financeTypeList)
    heatingType = random.choice(heatingTypeList)

    titleStr = objectType.type_name + "::" + str(random.randint(1,1000))
    shortDescription = financeType.type_name + "::" + heatingType.type_name

    Offer.objects.create(
        user=request.user,
        object_type=objectType,
        finance_type=financeType,
        heating_type=heatingType,
        title=titleStr,
        short_description=shortDescription,
        number_adults=random.randint(1,4),
        number_couples=random.randint(1,4),
        number_childern=random.randint(1,4),
        pets_number=random.randint(1,4),
        pets_are_allowed=random.randint(0,1),
        number_cars=random.randint(1,4),
        number_homeoffice=random.randint(1,4),
        number_kitchens=random.randint(1,4),
        number_bathrooms=random.randint(1,4),
        number_bedrooms=random.randint(1,4),
        living_area=random.randint(40,250),
        is_modern=random.randint(0,1),
        is_built_sustainable=random.randint(0,1),
        is_available_now=random.randint(0,1),
        living_floor=random.randint(0,10),
    )
