from django.db import models

# Create your models here.
#displaying trial events
class TrialEvent(models.Model):
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    date = models.DateField()
    description = models.TextField()
    banner_image = models.ImageField(upload_to='trials/images/')
    registration_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#for registring trails
class TrialRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preferred_position = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    passport_photo = models.ImageField(upload_to='registrations/passports/')
    event = models.ForeignKey(TrialEvent, on_delete=models.CASCADE, related_name='registrations')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.event.title}"
