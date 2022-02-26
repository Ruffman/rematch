from django.urls import path

from . import views

app_name = "matching"
urlpatterns = [
    path(
        "<str:object_type>/<int:object_id>/detail/",
        views.RecommendedMatchDetailView.as_view(),
        name="rec_match_detail",
    )
]
