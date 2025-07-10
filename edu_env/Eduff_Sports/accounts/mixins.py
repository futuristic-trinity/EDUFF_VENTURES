from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden

class ManagerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin to restrict access to users who are logged in and have is_manager=True
    """
    def test_func(self):
        return self.request.user.is_authenticated and getattr(self.request.user, 'is_manager', False)

    def handle_no_permission(self):
        return HttpResponseForbidden("You do not have permission to access this page.")
