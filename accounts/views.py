from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

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


class UpdateProfileDataView(UpdateView, LoginRequiredMixin):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    fields = [
        "username",
        "password",
        "email",
        "title",
        "academic_title",
        "vocation",
        "first_name",
        "last_name",
        "bio",
        "city_name",
        "zip_code",
        "birth_date",
    ]

    def get_success_url(self):
        view_name = "accounts:acc_profile"
        # in urls.py the slug is set to username, that's why you use it as kwarg
        # to find the profile view again after the username got changed
        return reverse(view_name, kwargs={"username": self.object.username})
