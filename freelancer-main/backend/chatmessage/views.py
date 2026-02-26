from rest_framework import generics, permissions
from django.db.models import Q
from .models import ChatMessage
from .serializers import ChatMessageSerializer


class ChatHistoryView(generics.ListAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        other_user_id = self.kwargs['other_user_id']

        return ChatMessage.objects.filter(
            (Q(sender=user) & Q(receiver_id=other_user_id)) |
            (Q(sender_id=other_user_id) & Q(receiver=user))
        ).order_by('timestamp')


class SendMessageView(generics.CreateAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)