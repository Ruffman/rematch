from itertools import chain

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from django.views import generic
from django.http import Http404

from insertions.models import (
    Offer,
    Request,
    Object_Address,
    Object_Location_Detail,
    Recreation_Area_Detail,
    Facility_Detail,
)

from accounts.models import User
from .models import Proposed_Match

# This view is called to look at the details of a matching opposite object
# If called by an OfferDetailView it display a matching request and vice versa
class RecommendedMatchDetailView(LoginRequiredMixin, generic.ListView):
    template_name = "matching_recommended_detail.html"

    # used to go back to the object that has led to the display of this view
    return_object_id = 0
    return_object_type = ""

    def set_return_values(self):
        prop_match = Proposed_Match.objects.get(pk=self.kwargs["prop_match_id"])
        if self.type == Offer.__name__:
            self.return_object_type = Request.__name__
            self.return_object_id = prop_match.request_id
        elif self.type == Request.__name__:
            self.return_object_type = Offer.__name__
            self.return_object_id = prop_match.offer.id

    def get_queryset(self, **kwargs):
        try:  # TODO: optimize so match_queryset is a subset of insertion objects and likes are no unnecessary querys
            self.id = self.kwargs["object_id"]
            self.type = self.kwargs["object_type"]

            if self.type == Offer.__name__:
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

                # self.like_queryset = Offer_Like.objects.filter(
                #     offer_id=self.id
                # )
            elif self.type == Request.__name__:
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

                # offer_id_queryset = Proposed_Match.objects.filter(
                #     request_id=self.id
                # ).values("offer_id")
                # self.proposed_match_queryset = Offer.objects.filter(
                #     id__in=offer_id_queryset
                # )
                #
                # self.like_queryset = Request_Like.objects.filter(
                #     request_id=self.id
                # )
            else:
                raise Http404
        except:
            raise Http404
        else:
            self.object_user_query = User.objects.get(id=self.object_query.user_id)
            self.set_return_values()

            return chain(
                self.object_query,
                self.object_user_query,
                self.object_address_queryset,
                self.object_location_detail_query,
                self.object_recreation_area_detail_query,
                self.object_facility_detail_query,
                # self.proposed_match_queryset,
                # self.like_queryset,
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.object_query
        context["user"] = self.object_user_query
        context["object_address"] = self.object_address_queryset
        context["object_location_detail"] = self.object_location_detail_query
        context[
            "recreation_area_detail"
        ] = self.object_recreation_area_detail_query
        context["facility_detail"] = self.object_facility_detail_query
        # context["proposed_match_list"] = self.proposed_match_queryset
        # context["like_list"] = self.like_queryset

        return context
