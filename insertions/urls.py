from django.urls import path



from . import views

app_name = 'insertions'
urlpatterns = [
    path('insert/', views.InsertView.as_view(), name='insert'),
    path('overview/', views.OverviewView.as_view(), name='overview'),
]
