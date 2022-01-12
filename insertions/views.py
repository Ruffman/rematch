from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from insertions.models import Object, Offer



# Create your views here.
class InsertView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'insert.html'
    fields = ('object_type', 'zip_code', 'city_name', 'street_name', 'street_number', 'living_area',
              'monthly_rent_price', 'buy_price')
    model = Object
    success_url = reverse_lazy('insertions:overview')

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)

class NewOfferView(InsertView):
    success_url = reverse_lazy('insertions:overview')


class OverviewView(TemplateView):
    template_name = 'overview.html'
