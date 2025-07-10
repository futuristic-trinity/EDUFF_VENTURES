from django.db import models
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=10)
    upi = models.CharField(max_length=10, unique=True, editable=False)
    position = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='players/images/')
    video = models.FileField(upload_to='players/videos/', blank=True, null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    #function to generate the upi 
    def generate_upi(self):
        base = slugify(self.name).upper()
        dob_part = self.date_of_birth.strftime('%d%m%y')
        return (base + dob_part)[:10]
    
    def save(self, *args, **kwargs):
        if not self.upi:
            self.upi = self.generate_upi()
            original_upi = self.upi
            counter = 1
            while Player.objects.filter(upi=self.upi).exists():
                self.upi = f"{original_upi[:8]}{counter}"
                counter += 1

        super().save(*args, **kwargs)        

    
    def __str__(self):
        return self.name
