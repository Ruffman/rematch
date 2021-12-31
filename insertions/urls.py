from django.urls import path



from . import views

appname = 'insertions'
urlpatterns = [
    path('insert/', views.InsertView.as_view(), name='insert'),
]
