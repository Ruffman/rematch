from django.views.generic import DetailView


# Create your views here.
class ConversationOverView(DetailView):
    template_name = "conversation_overview.html"
