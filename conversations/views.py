from django.views import generic

# Create your views here.
class ConversationOverView(generic.TemplateView):
    template_name = 'conversation_overview.html'
