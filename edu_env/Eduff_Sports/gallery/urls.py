
from django.urls import path
from .views import GalleryImageListView

#urls
urlpatterns = [ 

    path('', GalleryImageListView.as_view(), name='gallery'),
    
    
]