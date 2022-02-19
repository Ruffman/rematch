from itertools import chain

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

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
                self.object_query = Offer.objects.get(id=self.id)

                # TODO: split important addresses into extra set. there needs to be eval to guarantee only one normal address exists for an object
                self.object_address_queryset = Object_Address.objects.get(
                    offer_id=self.id
                )

                self.object_location_detail_query = (
                    Object_Location_Detail.objects.get(offer_id=self.id)
                )

                self.object_recreation_area_detail_query = (
                    Recreation_Area_Detail.objects.get(offer_id=self.id)
                )

                self.object_facility_detail_query = (
                    Facility_Detail.objects.get(offer_id=self.id)
                )

                request_id_queryset = Proposed_Match.objects.filter(
                    offer_id=self.id
                ).values("request_id")
                self.proposed_match_queryset = Request.objects.filter(
                    id__in=request_id_queryset
                )

                self.like_queryset = Offer_Like.objects.filter(
                    offer_id=self.id
                )
            elif self.kwargs["type"] == Request.__name__:
                self.object_query = Request.objects.get(id=self.id)

                # TODO: split important addresses into extra set. there needs to be eval to guarantee only one normal address exists for an object
                self.object_address_queryset = Object_Address.objects.get(
                    request_id=self.id
                )

                self.object_location_detail_query = (
                    Object_Location_Detail.objects.get(request_id=self.id)
                )

                self.object_recreation_area_detail_query = (
                    Recreation_Area_Detail.objects.get(request_id=self.id)
                )

                self.object_facility_detail_query = (
                    Facility_Detail.objects.get(request_id=self.id)
                )

                offer_id_queryset = Proposed_Match.objects.filter(
                    request_id=self.id
                ).values("offer_id")
                self.proposed_match_queryset = Offer.objects.filter(
                    id__in=offer_id_queryset
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
                self.object_query,
                self.object_address_queryset,
                self.object_location_detail_query,
                self.object_recreation_area_detail_query,
                self.object_facility_detail_query,
                self.proposed_match_queryset,
                self.like_queryset,
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.object_query
        context["object_address"] = self.object_address_queryset
        context["object_location_detail"] = self.object_location_detail_query
        context[
            "recreation_area_detail"
        ] = self.object_recreation_area_detail_query
        context["facility_detail"] = self.object_facility_detail_query
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


class NewInsertionView(LoginRequiredMixin, CreateWithInlinesView):
    inlines = (
        ObjectLocationDetailInline,
        RecreationAreaTypeInline,
        ObjectAddressInline,
        FacilityTypesInline,
    )
    base_fields = (
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
    )
    template_name = "insert.html"
    success_url = reverse_lazy("insertions:ins_overview")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        return super().form_valid(form)


class NewOfferView(NewInsertionView):
    model = Offer
    model_fields = (
        "monthly_rent_cold",
        "monthly_incidentals_price",
        "buy_price",
        "security_deposit",
    )

    def __init__(self):
        self.fields = self.base_fields + self.model_fields


class NewRequestView(NewInsertionView):
    model = Request
    model_fields = (
        "monthly_income",
        "available_cash",
    )

    def __init__(self):
        self.fields = self.base_fields + self.model_fields


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
