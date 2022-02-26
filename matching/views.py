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

# Create your views here.
class RecommendedMatchDetailView(LoginRequiredMixin, generic.ListView):
    template_name = "matching_recommended_detail.html"

    def get_queryset(self, **kwargs):
        try:  # TODO: optimize so match_queryset is a subset of insertion objects and likes are no unnecessary querys
            self.id = self.kwargs["object_id"]
            if self.kwargs["object_type"] == Offer.__name__:
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
            elif self.kwargs["object_type"] == Request.__name__:
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
