from django.db import models



from insertions.models import Offer, Request

# Create your models here.
class Match(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)



class OfferSentLikes(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)



class OfferReceivedLikes(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)



class RequestSentLikes(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)



class RequestReceivedLikes(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
