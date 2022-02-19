from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Offer)
admin.site.register(models.Request)
admin.site.register(models.Finance_Type)
admin.site.register(models.Heating_Type)
admin.site.register(models.Object_Type)
