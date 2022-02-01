from itertools import chain

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from extra_views import (
    CreateWithInlinesView,
    UpdateWithInlinesView,
    InlineFormSetFactory,
)

from insertions.models import (
    Offer,
    Request,
    Object_Address,
    Object_Location_Detail,
    Recreation_Area_Detail,
    Facility_Detail,
)
from matching.models import Offer_Like, Proposed_Match, Request_Like

# Create your views here.

# displays a detail view of an insertion(offer or request) with a list of possible matches,
# a list of sent sent_likes and a list of received likes TODO
class InsertionDetailView(LoginRequiredMixin, generic.ListView):
    template_name = "insertion_detail.html"

    def get_queryset(self, **kwargs):
        try:  # TODO: optimize so match_queryset is a subset of insertion objects and likes are no unnecessary querys
            self.id = self.kwargs["id"]
            if self.kwargs["type"] == Offer.__name__:
                self.object_queryset = Offer.objects.get(id=self.id)
                self.request_id_queryset = Proposed_Match.objects.filter(
                    offer_id=self.id
                ).values("request_id")
                self.proposed_match_queryset = Request.objects.filter(
                    id__in=self.request_id_queryset
                )
                self.like_queryset = Offer_Like.objects.filter(
                    offer_id=self.id
                )
            elif self.kwargs["type"] == Request.__name__:
                self.object_queryset = Request.objects.get(id=self.id)
                self.offer_id_queryset = Proposed_Match.objects.filter(
                    request_id=self.id
                ).values("offer_id")
                self.proposed_match_queryset = Offer.objects.filter(
                    id__in=self.offer_id_queryset
                )
                self.like_queryset = Request_Like.objects.filter(
                    request_id=self.id
                )
            else:
                raise Http404
        except:
            raise Http404
        else:
            return chain(
                self.object_queryset,
                self.proposed_match_queryset,
                self.like_queryset,
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.object_queryset
        context["proposed_match_list"] = self.proposed_match_queryset
        context["like_list"] = self.like_queryset

        return context


class ObjectAddressInline(InlineFormSetFactory):
    model = Object_Address
    fields = ("zip_code", "city_name", "street_name", "street_number")


class ObjectLocationDetailInline(InlineFormSetFactory):
    model = Object_Location_Detail
    fields = (
        "is_sunny",
        "is_calm",
        "at_hillside",
        "near_public_transport",
        "near_freeway",
        "near_stores",
        "near_recreation",
        "near_education",
        "has_nice_view",
    )


class RecreationAreaTypeInline(InlineFormSetFactory):
    model = Recreation_Area_Detail
    fields = (
        "has_balcony",
        "has_roof_terrace",
        "has_terrace",
        "has_garden",
        "has_winter_garden",
        "has_loggia",
        "something_different",
    )


class FacilityTypesInline(InlineFormSetFactory):
    model = Facility_Detail
    fields = (
        "has_storeroom",
        "has_carport",
        "has_fitted_kitchen",
        "has_elevator",
        "has_garage",
        "has_cellar",
        "has_parking_area",
        "is_furnished",
        "is_barrier_free",
        "is_partially_furnished",
    )


class NewOfferView(LoginRequiredMixin, CreateWithInlinesView):
    model = Offer
    inlines = (
        ObjectLocationDetailInline,
        RecreationAreaTypeInline,
        ObjectAddressInline,
        FacilityTypesInline,

    )
    fields = (
        "object_type",
        "finance_type",
        "heating_type",
        "title",
        "short_description",
        "number_adults",
        "number_couples",
        "number_children",
        "pets_number",
        "pets_are_allowed",
        "number_cars",
        "number_homeoffice",
        "number_kitchens",
        "number_bathrooms",
        "number_bedrooms",
        "living_area",
        "living_floor",
        "is_modern",
        "is_built_sustainable",
        "is_available_now",
        "available_at_date",
        "monthly_rent_cold",
        "monthly_incidentals_price",
        "buy_price",
        "security_deposit",
    )
    template_name = "insert.html"
    success_url = reverse_lazy("insertions:ins_overview")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


class NewRequestView(LoginRequiredMixin, generic.edit.CreateView):
    model = Request
    fields = (
        "object_type",
        "zip_code",
        "city_name",
        "street_name",
        "street_number",
        "living_area",
        "monthly_rent_price",
        "buy_price",
    )
    template_name = "insert.html"
    success_url = reverse_lazy("insertions:ins_overview")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


class InsertionOverView(LoginRequiredMixin, generic.ListView):
    template_name = "insertion_overview.html"

    def get_queryset(self):
        try:
            current_user_id = self.request.user.id
            self.offer_queryset = Offer.objects.filter(user_id=current_user_id)
            self.request_queryset = Request.objects.filter(
                user_id=current_user_id
            )
        except:
            raise Http404
        else:
            return chain(self.offer_queryset, self.request_queryset)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offer_list"] = self.offer_queryset
        context["request_list"] = self.request_queryset
        return context
