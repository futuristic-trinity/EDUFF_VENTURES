from django.urls import path
from .views import (
    TrialListView,
    TrialDetailView,
    TrialCreateView,
    TrialUpdateView,
    TrialDeleteView,
    TrialRegistrationView,
)

app_name = 'trials'

urlpatterns = [
    path('', TrialListView.as_view(), name='trial-list'),
    path('<int:pk>/', TrialDetailView.as_view(), name='trial-detail'),
    path('create/', TrialCreateView.as_view(), name='trial-create'),
    path('<int:pk>/update/', TrialUpdateView.as_view(), name='trial-update'),
    path('<int:pk>/delete/', TrialDeleteView.as_view(), name='trial-delete'),
    path('register/<int:event_id>/', TrialRegistrationView.as_view(), name='register_trial'),
]
