from django.db import models

from insertions.models import Offer, Request


# Create your models here.
# table for the matches we recommend User
class Proposed_Match(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)


# table for storing matches where both user liked the other party
class True_Match(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)


# sent and received likes based on an offer object
class Offer_Like(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    sent_like_to_request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name="sentLikeTo"
    )
    received_like_from_request = models.ForeignKey(
        Request, on_delete=models.CASCADE, related_name="receivedLikeFrom"
    )


# sent and received likes based on a request object
class Request_Like(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    sent_like_to_offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, related_name="sentLikeTo"
    )
    received_like_from_offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, related_name="receivedLikeFrom"
    )
