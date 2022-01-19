from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from . import forms



# Create your views here.
class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'signup.html'

class ProfileView(DetailView, LoginRequiredMixin):
    template_name = 'accounts_profile.html'
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
