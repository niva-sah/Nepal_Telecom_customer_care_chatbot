from django.urls import path
from .views import chat_page, chat_api

urlpatterns = [
    path('', chat_page, name='chat_page'),
    path('chat_api/', chat_api, name='chat_api'),  
]