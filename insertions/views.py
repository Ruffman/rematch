from itertools import chain

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from insertions.models import Object, Offer, Request
from matching.models import Offer_Like, Proposed_Match, Request_Like

# Create your views here.

# displays a detail view of an insertion(offer or request) with a list of possible matches,
# a list of sent sent_likes and a list of received likes TODO
class InsertionDetailView(LoginRequiredMixin, generic.ListView):
    template_name = 'insertion_detail.html'

    def get_queryset(self, **kwargs):
        try: # TODO: optimize so match_queryset is a subset of insertion objects and likes are no unnecessary querys
            self.id = self.kwargs['id']
            if self.kwargs['type'] == Offer.__name__:
                self.object_queryset = Offer.objects.get(id=self.id)
                self.request_id_queryset = Proposed_Match.objects.filter(offer_id=self.id).values('request_id')
                self.proposed_match_queryset = Request.objects.filter(id__in=self.request_id_queryset)
                self.like_queryset = Offer_Like.objects.filter(offer_id=self.id)
            elif self.kwargs['type'] == Request.__name__:
                self.object_queryset = Request.objects.get(id=self.id)
                self.offer_id_queryset = Proposed_Match.objects.filter(request_id=self.id).values('offer_id')
                self.proposed_match_queryset = Offer.objects.filter(id__in=self.offer_id_queryset)
                self.like_queryset = Request_Like.objects.filter(request_id=self.id)
            else:
                raise Http404
        except:
            raise Http404
        else:
            return chain(self.object_queryset, self.proposed_match_queryset, self.like_queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object_queryset
        context['proposed_match_list'] = self.proposed_match_queryset
        context['like_list'] = self.like_queryset

        return context



class NewOfferView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'insert.html'
    fields = ('object_type', 'zip_code', 'city_name', 'street_name', 'street_number', 'living_area',
              'monthly_rent_price', 'buy_price')
    model = Offer
    success_url = reverse_lazy('insertions:ins_overview')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)



class NewRequestView(LoginRequiredMixin, generic.edit.CreateView):
    template_name = 'insert.html'
    fields = ('object_type', 'zip_code', 'city_name', 'street_name', 'street_number', 'living_area',
              'monthly_rent_price', 'buy_price')
    model = Request
    success_url = reverse_lazy('insertions:ins_overview')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)



class InsertionOverView(LoginRequiredMixin, generic.ListView):
    template_name = 'insertion_overview.html'

    def get_queryset(self):
        try:
            current_user_id = self.request.user.id
            self.offer_queryset = Offer.objects.filter(user_id=current_user_id)
            self.request_queryset = Request.objects.filter(user_id=current_user_id)
        except:
            raise Http404
        else:
            return chain(self.offer_queryset, self.request_queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offer_list'] = self.offer_queryset
        context['request_list'] = self.request_queryset
        return context
