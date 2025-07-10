from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name='home'),

    # Players
    path('players/', views.PlayerListView.as_view(), name='player_list'),
    path('players/add/', views.PlayerCreateView.as_view(), name='add_player'),
    path('players/edit/<int:pk>/', views.PlayerUpdateView.as_view(), name='edit_player'),
    path('players/delete/<int:pk>/', views.PlayerDeleteView.as_view(), name='delete_player'),

    # Gallery
    path('gallery/', views.GalleryListView.as_view(), name='gallery_list'),
    path('gallery/add/', views.GalleryCreateView.as_view(), name='add_image'),
    path('gallery/delete/<int:pk>/', views.GalleryDeleteView.as_view(), name='delete_image'),

    # Trials
    path('trials/', views.TrialListView.as_view(), name='trial_list'),
    path('trials/add/', views.TrialCreateView.as_view(), name='trial_create'),
    path('trials/edit/<int:pk>/', views.TrialUpdateView.as_view(), name='edit_trial'),
    path('trials/delete/<int:pk>/', views.TrialDeleteView.as_view(), name='delete_trial'),

    # Registrations
    path('registrations/<int:trial_id>/', views.RegistrationListView.as_view(), name='registration_list'),

    # Contact Messages
    path('messages/', views.MessageListView.as_view(), name='messages'),
    path('messages/<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
    path('messages/delete/<int:pk>/', views.MessageDeleteView.as_view(), name='delete_message'),
    
    #reply messages
    path('messages/<int:pk>/reply/', views.ReplyMessageView.as_view(), name='reply_message'),
]
