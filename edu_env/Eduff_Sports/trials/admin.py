from django.contrib import admin
from .models import TrialEvent,TrialRegistration


# Register your models here.

@admin.register(TrialEvent)
class TrialEventadmin(admin.ModelAdmin):
    list_display = ('title', 'registration_link', 'location', 'start_date', 'end_date', 'register_fees')
    search_fields = ('title', 'start_date')


@admin.register(TrialRegistration)
class TrialRegistrationadmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'submitted_at', 'preferred_position', 'location', 'status')
    search_fields = ('full_name', 'preferred_position', 'location')
