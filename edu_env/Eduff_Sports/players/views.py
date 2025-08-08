from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Player
#from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import ManagerRequiredMixin 

# Create your views here.
app_name = 'players'
class PlayerListView(ListView):
    model= Player
    template_name = 'players/player_list.html'
    context_object_name = 'players'



class PlayerDetailView(DetailView):
    model= Player
    template_name = 'players/player_detail.html'
    context_object_name = 'player'



class PlayerCreateView(ManagerRequiredMixin, CreateView):
    model = Player
    fields = '__all__'
    template_name = 'players/player_form.html'
    success_url = reverse_lazy('manager:player_list')



class PlayerUpdateView( ManagerRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'players/player_form.html'
    success_url = reverse_lazy('accounts:dashboard')


class PlayerDeleteView( ManagerRequiredMixin, DeleteView):
    model = Player
    fields = '__all__'
    template_name = 'players/player_confirm_delete.html'
    success_url = reverse_lazy('manager:player_list')