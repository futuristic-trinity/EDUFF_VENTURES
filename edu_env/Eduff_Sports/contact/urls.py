from django.urls import path
from .views import ContactCreateView, ContactMessageListView

app_name = 'contact'
urlpatterns = [
    path('', ContactCreateView.as_view(), name='contact'),
    path('messages/', ContactMessageListView.as_view(), name='contact_list'),
    
]

