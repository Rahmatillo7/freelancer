from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Notification
        fields = ['id', 'user', 'user_name', 'type', 'message', 'read_status', 'timestamp']
        read_only_fields = ['user', 'read_status', 'timestamp']