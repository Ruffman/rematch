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

# displays a detail view of an insertion(offer or request) with a list of possible matches,
# a list of sent sent_likes and a list of received likes
class InsertionDetailView(LoginRequiredMixin, generic.ListView):
    template_name = 'insertion_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

class NewOfferView(InsertView):
    success_url = reverse_lazy('insertions:overview')


class OverviewView(LoginRequiredMixin, generic.ListView):
    model = Object
    template_name = 'overview.html'

    # def get_queryset(self):
    #     return Object.objects.all() # TODO: filter by current user_id
    #
    # def get_context_data(self, **kwargs):
    #     return super().get_context_data(**kwargs)
