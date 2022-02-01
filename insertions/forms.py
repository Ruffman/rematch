from django import forms

from . import models


class InsertionForm(forms.ModelForm):
    class Meta:
        fields = "user_id"
        model = models.Offer

    user_id = forms.CharField(max_length=100)
