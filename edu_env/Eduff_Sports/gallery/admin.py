from django.contrib import admin
from .models import GalleryImage

# Register your models here.

@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'uploaded_at')
    search_fields = ('title',)