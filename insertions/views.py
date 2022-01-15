from itertools import chain

from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from insertions.models import Object, Offer, Request



# Create your views here.

# displays a detail view of an insertion(offer or request) with a list of possible matches,
# a list of sent sent_likes and a list of received likes TODO
class InsertionDetailView(LoginRequiredMixin, generic.ListView):
    template_name = 'insertion_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



class NewOfferView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'insert.html'
    fields = ('object_type', 'zip_code', 'city_name', 'street_name', 'street_number', 'living_area',
              'monthly_rent_price', 'buy_price')
    model = Offer
    success_url = reverse_lazy('insertions:overview')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)



class NewRequestView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'insert.html'
    fields = ('object_type', 'zip_code', 'city_name', 'street_name', 'street_number', 'living_area',
              'monthly_rent_price', 'buy_price')
    model = Request
    success_url = reverse_lazy('insertions:overview')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)



class OverviewView(LoginRequiredMixin, generic.ListView):
    template_name = 'overview.html'

    def get_queryset(self):
        offer_queryset = Offer.objects.all()
        request_queryset = Request.objects.all()
        queryset = chain(offer_queryset, request_queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offer_list'] = Offer.objects.all()
        context['request_list'] = Request.objects.all()
        return context
