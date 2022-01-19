from django.urls import path

from . import views



app_name = 'matching'
urlpatterns = [
    path('<str:type>/<int:id>/detail/', views.RecommendedMatchDetailView.as_view(), name='rec_match_detail')
]
