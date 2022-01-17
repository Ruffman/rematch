from itertools import chain

from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404

from insertions.models import Object, Offer, Request
from matching.models import ProposedMatch, OfferLike, RequestLike



# Create your views here.

# displays a detail view of an insertion(offer or request) with a list of possible matches,
# a list of sent sent_likes and a list of received likes TODO
class InsertionDetailView(LoginRequiredMixin, generic.ListView):
    template_name = 'insertion_detail.html'

    def get_queryset(self, **kwargs):
        try:
            if self.kwargs['type'] == 'offer':
                self.object_queryset = Offer.objects.get(id=self.kwargs['id'])
                self.proposed_match_queryset = ProposedMatch.objects.filter(offer_id=self.kwargs['id'])
                self.like_queryset = OfferLike.objects.filter(offer_id=self.kwargs['id'])
            elif self.kwargs['type'] == 'request':
                self.object_queryset = Request.objects.get(id=self.kwargs['id'])
                self.proposed_match_queryset = ProposedMatch.objects.filter(request_id=self.kwargs['id'])
                self.like_queryset = RequestLike.objects.filter(request_id=self.kwargs['id'])
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
        offer_queryset = Offer.objects.all()
        request_queryset = Request.objects.all()
        queryset = chain(offer_queryset, request_queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['offer_list'] = Offer.objects.all()
        context['request_list'] = Request.objects.all()
        return context
