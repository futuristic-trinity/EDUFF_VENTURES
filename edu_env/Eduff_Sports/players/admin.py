from django.contrib import admin
from .models import Player


# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'upi', 'position', 'profile_image' , 'video', 'created_at')
    search_fields = ('name', 'position')
