from django.db import models

from insertions.models import Offer, Request


# Create your models here.
class Proposed_Match(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    offer_like = models.BooleanField(default=False)
    request_like = models.BooleanField(default=False)
    true_match = models.BooleanField(default=False)

    class Meta:
        unique_together = ("offer", "request")
