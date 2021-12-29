from django.views.generic import TemplateView




class BasePage(TemplateView):
    template_name = 'base.html'
