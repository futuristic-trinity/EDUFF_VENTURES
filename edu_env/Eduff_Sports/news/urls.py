# urls.py
from django.urls import path
from .views import (
    NewsPostListView,
    NewsPostDetailView,
    NewsPostCreateView,
    NewsPostUpdateView,
    NewsPostDeleteView
)

app_name = 'news'

urlpatterns = [
    path('', NewsPostListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsPostDetailView.as_view(), name='news_detail'),
    path('create/', NewsPostCreateView.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsPostUpdateView.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsPostDeleteView.as_view(), name='news_delete'),
]
