from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    receiver_username = serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = ChatMessage
        fields = ['id', 'sender', 'sender_username', 'receiver', 'receiver_username', 'message', 'timestamp', 'read_status']
        read_only_fields = ['sender', 'timestamp', 'read_status']