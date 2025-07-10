from django.views.generic import CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from .models import ContactMessage
from accounts.mixins import ManagerRequiredMixin

class ContactCreateView(CreateView):
    model = ContactMessage
    fields = '__all__'
    template_name = 'contact.html'
    success_url = reverse_lazy('thankyou')

# Manager: View all contact messages
class ContactMessageListView(ManagerRequiredMixin, ListView):
    model = ContactMessage
    template_name = 'contact.html'
    context_object_name = 'messages'
    ordering = ['-created_at']


class ContactDeleteView(ManagerRequiredMixin, DeleteView):
    model = ContactMessage
    template_name = 'contact.html'
    #success_url = reverse_lazy('manager:contact_list')
