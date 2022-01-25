from django.views.generic import TemplateView


# Create your views here.
class RecommendedMatchDetailView(TemplateView):
    template_name = 'matching_recommended_detail.html'
