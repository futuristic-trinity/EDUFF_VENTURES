from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NewsPost
from .forms import NewsPostForm

class NewsPostListView(ListView):
    model = NewsPost
    template_name = 'dashboard/news_list.html'
    context_object_name = 'news_list'
    ordering = ['-created_at']

class NewsPostDetailView(DetailView):
    model = NewsPost
    template_name = 'news_detail.html'

class NewsPostCreateView(CreateView):
    model = NewsPost
    form_class = NewsPostForm
    template_name = 'news_create.html'
    success_url = reverse_lazy('news_list')

class NewsPostUpdateView(UpdateView):
    model = NewsPost
    form_class = NewsPostForm
    template_name = 'dashboard/news_update.html'
    success_url = reverse_lazy('news:news_list')

class NewsPostDeleteView(DeleteView):
    model = NewsPost
    template_name = 'dashboard/news_comfirm_delete.html'
    success_url = reverse_lazy('news:news_list')