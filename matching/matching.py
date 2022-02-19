# here all functionality for finding matches will go
from insertions.models import Offer, Request
from matching.models import Proposed_Match



def generate_proposed_matches_for_request(instance):
    print('generate_proposed_matches_for_request')
    matches_query = Offer.objects.filter(object_type_id = instance.object_type_id) # TODO: here needs to go a proper matching algo
    for match in matches_query:
        Proposed_Match.objects.create(offer=match, request=instance)

def generate_proposed_matches_for_offer(instance):
    print('generate_proposed_matches_for_offer')
    matches_query = Request.objects.filter(object_type_id = instance.object_type_id) # TODO: here needs to go a proper matching algo
    for match in matches_query:
        Proposed_Match.objects.create(offer=instance, request=match)

def lookup_matches_for_request(instance):
    generate_proposed_matches_for_request(instance)


def lookup_matches_for_offer(instance):
    generate_proposed_matches_for_offer(instance)


def lookup_matches(instance):
    if instance.__class__.__name__ == "Request":
        lookup_matches_for_request(instance)

    elif instance.__class__.__name__ == "Offer":
        lookup_matches_for_offer(instance)
