from django.dispatch import receiver
from django.db.models.signals import post_save

from . import matching
from insertions.models import Object


@receiver(post_save, sender=Object)
def look_for_matches(sender, **kwargs):
    matching.lookup_matches(sender)
