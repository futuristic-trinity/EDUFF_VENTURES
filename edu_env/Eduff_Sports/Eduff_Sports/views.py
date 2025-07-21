# Eduff_Ventures/views.py
from django.views.generic import TemplateView
from players.models import Player
from trials.models import TrialEvent
from gallery.models import GalleryImage
from news.models import NewsPost


class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.all()
        context['trials'] = TrialEvent.objects.all()
        context['galleries'] = GalleryImage.objects.all()
        context["latest_news"] = NewsPost.objects.order_by("-created_at")[:4]
        return context



    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class ThankyouView(TemplateView):
    template_name = 'thankyou.html'