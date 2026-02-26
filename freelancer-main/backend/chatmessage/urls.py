from django.urls import path
from .views import ChatHistoryView, SendMessageView

urlpatterns = [
    path('send/', SendMessageView.as_view(), name='send-message'),
    path('history/<int:other_user_id>/', ChatHistoryView.as_view(), name='chat-history'),
]