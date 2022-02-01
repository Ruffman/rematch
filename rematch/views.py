from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = "test.html"


class BasePage(TemplateView):
    template_name = "base.html"


class LandingPage(TemplateView):
    template_name = "landing.html"
