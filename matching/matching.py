# here all functionality for finding matches will go
from insertions.models import Offer, Request


def lookup_matches_for_offer():
    query = Request.objects.all()
    print(query)


def lookup_matches_for_request():
    query = Offer.objects.all()
    print(query)
