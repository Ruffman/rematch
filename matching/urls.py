from django.urls import path

from . import views

app_name = "matching"
urlpatterns = [
    path(
        "<int:prop_match_id>/<str:object_type>/<int:object_id>/detail/",
        views.RecommendedMatchDetailView.as_view(),
        name="rec_match_detail",
    )
]
