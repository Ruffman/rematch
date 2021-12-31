from django.db import models



from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Offer(models.Model):
    user_id = models.ForeignKey(User, related_name='offer', on_delete=models.CASCADE)

class Request(models.Model):
    user_id = models.ForeignKey(User, related_name='request', on_delete=models.CASCADE)
