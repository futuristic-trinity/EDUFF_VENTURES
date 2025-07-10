from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import GalleryImage
from django.urls import reverse_lazy
from accounts.mixins import ManagerRequiredMixin

# Create your views here.

class GalleryImageListView(ListView):
    model = GalleryImage
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'
    ordering = ['-uploaded_at']


class GalleryCreateView(ManagerRequiredMixin, CreateView):
    model = GalleryImage
    fields = '__all__'
    template_name = 'manager/gallery_form.html'
    #success_url = reverse_lazy('manager:gallery_list')


class GalleryUpdateView(ManagerRequiredMixin, UpdateView):
    model = GalleryImage
    fields = '__all__'
    template_name = 'manager/gallery_form.html'
    #success_url = reverse_lazy('manager:gallery_list')


class GalleryDeleteView(ManagerRequiredMixin, DeleteView):
    model = GalleryImage
    template_name = 'manager/gallery_confirm_delete.html'
    #success_url = reverse_lazy('manager:gallery_list')   