from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='accounts/profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username
