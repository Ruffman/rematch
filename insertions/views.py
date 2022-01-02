from django.views.generic import TemplateView



# Create your views here.
class InsertView(TemplateView):
    template_name = 'insert.html'

class OverviewView(TemplateView):
    template_name = 'overview.html'
