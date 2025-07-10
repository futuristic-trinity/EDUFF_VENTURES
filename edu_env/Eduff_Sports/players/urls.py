from django.urls import path
from .views import PlayerListView, PlayerDetailView, PlayerCreateView,PlayerDeleteView, PlayerUpdateView

app_name = 'players' 

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),



    # Dashboard-specific routes
    path('dashboard/', PlayerListView.as_view(), name='player_list'),
    path('dashboard/add/', PlayerCreateView.as_view(), name='player_add'),
    path('dashboard/<int:pk>/edit/', PlayerUpdateView.as_view(), name='player_edit'),
    path('dashboard/<int:pk>/delete/', PlayerDeleteView.as_view(), name='player_delete'),
    
]











