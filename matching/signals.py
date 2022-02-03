from django.dispatch import receiver
from django.db.models.signals import post_save

from . import matching
from insertions.models import Offer, Request


@receiver(post_save, sender=Offer)
def look_for_matches_for_offer(sender, **kwargs):
    print("looking for matches offer")
    matching.lookup_matches_for_offer()


@receiver(post_save, sender=Request)
def look_for_matches_for_request(sender, **kwargs):
    print("looking for matches request")
    matching.lookup_matches_for_request()
