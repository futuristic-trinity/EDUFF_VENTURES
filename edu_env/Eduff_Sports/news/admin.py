from django.contrib import admin
from .models import NewsPost

# Register your models here.


@admin.register(NewsPost)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_url', 'created_at')
