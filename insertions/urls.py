from django.urls import path



from . import views

app_name = 'insertions'
urlpatterns = [
    path('new_offer/', views.NewOfferView.as_view(), name='new_offer'),
    path('new_request/', views.NewRequestView.as_view(), name='new_request'),
    path('overview/', views.InsertionOverView.as_view(), name='ins_overview'),
    path('detail/<int:id>', views.InsertionDetailView.as_view(), name='detail'),
]
