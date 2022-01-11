from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from insertions.models import Object



# Create your views here.
class InsertView(LoginRequiredMixin, generic.CreateView):
    template_name = 'insert.html'
    fields = ('object_type', 'zip_code', 'city_name', 'street_name', 'street_number', 'living_area',
              'monthly_rent_price', 'buy_price')
    model = Object

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('overview')

        return render(request, self.template_name, {'form':form})

class OverviewView(TemplateView):
    template_name = 'overview.html'
