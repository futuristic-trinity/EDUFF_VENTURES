from django.db import models
from django.utils import timezone
from urllib.parse import urlparse, parse_qs


# Create your models here.

class NewsPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='news_videos/', blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    is_local = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def is_youtube(self):
        return bool(self.youtube_url)
    
    #youtube embedding url for iframe display
    def embed_url(self):
        parsed_url = urlparse(self.youtube_url)
        youtube_id = parse_qs(parsed_url.query).get('v')
        if youtube_id:
            return f"https://www.youtube.com/embed/{youtube_id[0]}"
        return ""