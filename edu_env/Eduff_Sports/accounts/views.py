from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .forms import ManagerLoginForm
from django.contrib import messages
from django.shortcuts import redirect
from accounts.mixins import ManagerRequiredMixin
#from django.contrib.auth.mixins import LoginRequiredMixin
from players.models import Player


class ManagerDashboardView(ManagerRequiredMixin, TemplateView):
    template_name = 'dashboard_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['players'] = Player.objects.all()
        return context


class ManagerLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = ManagerLoginForm

    def form_valid(self, form):
        # Check if the user is a manager
        if form.get_user().is_manager:
            return super().form_valid(form)
        else:
            messages.error(self.request, "You do not have manager access.")
            return redirect('accounts:manager_login')
