# here all functionality for finding matches will go
from insertions.models import Offer, Request



def lookup_matching_offers(request):
    print("lookup matching offer")



def lookup_matching_requests(offer):
    print("lookup matching requests")


def lookup_matches(instance):
    if instance.__class__ == Request:
        lookup_matching_offers(instance)

    elif instance.__class__ == Offer:
        lookup_matching_requests(instance)
