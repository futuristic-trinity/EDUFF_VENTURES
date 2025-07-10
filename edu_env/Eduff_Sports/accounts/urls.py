from django.urls import path
from .views import ManagerDashboardView, ManagerLoginView


from django.views.generic import RedirectView

app_name = 'accounts'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='accounts:dashboard', permanent=False)),  # Redirect /accounts/ to /accounts/dashboard/
    path('dashboard/', ManagerDashboardView.as_view(), name='dashboard'),
    path('login/', ManagerLoginView.as_view(), name='manager_login'),
]

