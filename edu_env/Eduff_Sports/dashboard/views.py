
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView, UpdateView
from .forms import TrialEventForm, ReplyMessageForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from players.models import Player
from gallery.models import GalleryImage
from trials.models import TrialEvent, TrialRegistration
from contact.models import ContactMessage

# Dashboard Overview
class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['player_count'] = Player.objects.count()
        context['trial_count'] = TrialEvent.objects.count()
        context['message_count'] = ContactMessage.objects.count()
        context['gallery_count'] = GalleryImage.objects.count()
        return context

# Player Management
class PlayerListView(LoginRequiredMixin, ListView):
    model = Player
    template_name = 'dashboard/player_list.html'
    context_object_name = 'players'

class PlayerCreateView(LoginRequiredMixin, CreateView):
    model = Player
    fields = ['surname', 'first_name', 'date_of_birth', 'position', 'profile_image', 'video', 'description']
    template_name = 'dashboard/player_form.html'
    success_url = reverse_lazy('dashboard:player_list')

class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'dashboard/player_form.html'
    success_url = reverse_lazy('dashboard:player_list')

class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    template_name = 'dashboard/player_confirm_delete.html'
    success_url = reverse_lazy('dashboard:player_list')

# Gallery Management
class GalleryListView(LoginRequiredMixin, ListView):
    model = GalleryImage
    template_name = 'dashboard/gallery_list.html'
    context_object_name = 'images'

class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = GalleryImage
    fields = ['title', 'image']
    template_name = 'dashboard/gallery_form.html'
    success_url = reverse_lazy('dashboard:gallery_list')

class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = GalleryImage
    template_name = 'dashboard/gallery_confirm_delete.html'
    success_url = reverse_lazy('dashboard:gallery_list')

# Trial Events
class TrialListView(LoginRequiredMixin, ListView):
    model = TrialEvent
    template_name = 'dashboard/trials_list.html'
    context_object_name = 'trials'

class TrialCreateView(LoginRequiredMixin, CreateView):
    model = TrialEvent
    fields = '__all__'
    template_name = 'dashboard/trials_form.html'
    success_url = reverse_lazy('dashboard:trial_list')

class TrialUpdateView(LoginRequiredMixin, UpdateView):
    model = TrialEvent
    fields = '__all__'
    template_name = 'dashboard/trials_form.html'
    success_url = reverse_lazy('dashboard:trial_list')

class TrialDeleteView(LoginRequiredMixin, DeleteView):
    model = TrialEvent
    template_name = 'trials_confirm_delete.html'
    success_url = reverse_lazy('dashboard:trial_list')

# Trial Registrations
class RegistrationListView(ListView):
    model = TrialRegistration
    template_name = 'dashboard/registration_list.html'
    context_object_name = 'registrations'

    def get_queryset(self):
        trial_id = self.kwargs.get('trial_id')
        return TrialRegistration.objects.filter(event__id=trial_id)
    
#registrations approval
from django.views import View
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from trials.models import TrialRegistration
from django.core.mail import send_mail, BadHeaderError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class ApproveRegistrationView(View):
    def post(self, request, pk, *args, **kwargs):
        registration = get_object_or_404(TrialRegistration, pk=pk)

        # Send email
        try:
            validate_email(registration.email)
            send_mail(
                subject='Trial Registration Approved',
                message='Your trial registration has been approved. You will be contacted shortly to complete payment.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[registration.email],
                fail_silently=False,
            )
        except ValidationError:
            messages.error(request, "Invalid email address. Could not send notification.")
            return redirect('dashboard:registration_list',trial_id=registration.event.id)
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
            return redirect('dashboard:registration_list',trial_id=registration.event.id)
        except Exception as e:
            messages.error(request, f"Email send failed: {str(e)}")
            return redirect('dashboard:registration_list',trial_id=registration.event.id)




        registration.status = 'approved'
        registration.save()
        messages.success(request, f"{registration.full_name}'s registration approved.")
        return redirect('dashboard:registration_list', trial_id=registration.event.id)

class RejectRegistrationView(View):
    def post(self, request, pk, *args, **kwargs):
        registration = get_object_or_404(TrialRegistration, pk=pk)

        # Send email
        try:
            validate_email(registration.email)
            send_mail(
                subject='Trial Registration Rejected',
                message=(
                    f"Dear {registration.full_name},\n\n"
                    f"Your registration for '{registration.event.title}' has been rejected.\n"
                    "For any inquiries, please contact the event manager.\n"
                    "via whatsapp: +233-0248945288 or Call: +233-0543834753 "
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[registration.email],
                fail_silently=False,
            )
        except ValidationError:
            messages.error(request, "Invalid email address. Could not send notification.")
            return redirect('dashboard:registration_list',trial_id=registration.event.id)
        except BadHeaderError:
            messages.error(request, "Invalid header found.")
            return redirect('dashboard:registration_list',trial_id=registration.event.id)
        except Exception as e:
            messages.error(request, f"Email send failed: {str(e)}")
            return redirect('dashboard:registration_list',trial_id=registration.event.id)


        registration.status = 'rejected'
        registration.save()
        messages.warning(request, f"{registration.full_name}'s registration rejected.")
        return redirect('dashboard:registration_list', trial_id=registration.event.id)


# Contact Messages
class MessageListView(LoginRequiredMixin, ListView):
    model = ContactMessage
    template_name = 'dashboard/contact_messages.html'
    context_object_name = 'messages'

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = ContactMessage
    template_name = 'dashboard/message_detail.html'
    context_object_name = 'message'

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = ContactMessage
    template_name = 'dashboard/message_confirm_delete.html'
    success_url = reverse_lazy('dashboard:messages')


############# REPLYING MESSAGES #############
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class ReplyMessageView(View):
    def get(self, request, pk):
        message = get_object_or_404(ContactMessage, pk=pk)
        form = ReplyMessageForm(initial={'subject': f"Re: {message.subject}"})
        return render(request, 'dashboard/reply_message.html', {'form': form, 'message': message})

    def post(self, request, pk):
        message = get_object_or_404(ContactMessage, pk=pk)
        form = ReplyMessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [message.email],
                    fail_silently=False
                )
                messages.success(request, "Reply sent successfully to the sender.")
                return redirect('contact_messages')
            except Exception as e:
                messages.error(request, f"Failed to send email: {e}")
        return render(request, 'dashboard/reply_message.html', {'form': form, 'message': message})
