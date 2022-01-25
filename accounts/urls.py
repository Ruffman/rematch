from django.contrib.auth.urls import views as auth_views
from django.urls import include, path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<slug:username>/profile/', views.ProfileView.as_view(), name='acc_profile'),
]
