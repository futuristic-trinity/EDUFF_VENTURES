from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your models here.
#displaying trial events
class TrialEvent(models.Model):
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    start_date = models.DateField()#added
    end_date = models.DateField(blank=True, null=True)#added
    description = models.TextField()
    banner_image = models.ImageField(upload_to='trials/images/')
    register_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True) #new feature
    registration_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#for registring trails
class TrialRegistration(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preferred_position = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    passport_photo = models.ImageField(upload_to='registrations/passports/')
    event = models.ForeignKey(TrialEvent, on_delete=models.CASCADE, related_name='registrations')
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    note = models.TextField(blank=True, null=True)  # Manager remarks (optional)


    
    def clean(self):
        try:
            validate_email(self.email)
        except ValidationError:
            raise ValidationError("Invalid email address.")


    def __str__(self):
        return f"{self.full_name} - {self.event.title} ({self.status})"
