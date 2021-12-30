
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

from . import forms



# Create your views here.
class SignUpView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'signup.html'
