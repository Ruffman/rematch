from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import UserCreateForm
from .models import User

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "signup.html"


class ProfileView(DetailView, LoginRequiredMixin):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "accounts_profile.html"
