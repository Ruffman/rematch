from django.urls import path

from . import views

app_name = "conversations"
urlpatterns = [
    path(
        "conversation/",
        views.ConversationOverView.as_view(),
        name="con_overview",
    ),
]
