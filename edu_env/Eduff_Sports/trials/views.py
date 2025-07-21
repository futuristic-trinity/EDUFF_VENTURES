from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TrialEvent, TrialRegistration
from .forms import TrialRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.mixins import ManagerRequiredMixin

# === public view ===
# List of all trial events
class TrialListView( ListView):
    model = TrialEvent
    template_name = 'trials_summit.html'
    context_object_name = 'trials'
    ordering = ['-start_date']

class TrialDetailView(ManagerRequiredMixin, DetailView):
    model = TrialEvent
    template_name = 'trials_summit.html'

class TrialCreateView(ManagerRequiredMixin, CreateView):
    model = TrialEvent
    fields = '__all__'
    template_name = 'trials_summit.html'
    success_url = reverse_lazy('trial-list')

class TrialUpdateView(ManagerRequiredMixin, UpdateView):
    model = TrialEvent
    fields = '__all__'
    template_name = 'trials_summit.html'
    success_url = reverse_lazy('trial-list')

class TrialDeleteView(ManagerRequiredMixin, DeleteView):
    model = TrialEvent
    template_name = 'trials_confirm_delete.html'
    success_url = reverse_lazy('trial-list')

#rgistration view
class TrialRegistrationView(CreateView):
    model = TrialRegistration
    form_class = TrialRegistrationForm
    template_name = 'summit_form.html'
    success_url = reverse_lazy('trials:trial-list')  # Redirect after success


    def get_initial(self):
        initial = super().get_initial()
        event_id = self.kwargs.get('event_id')
        initial['event'] = event_id
        return initial
    
    def form_valid(self, form):
        messages.success(self.request, "You have successfully registered for the event!")
        return super().form_valid(form)

