from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.
class Chat(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(User)



class ChatLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    #received_at = models.DateTimeField()
    content_text = models.TextField(max_length=2047)
    content_image = models.ImageField(upload_to=None, height_field=None, width_field=None)
