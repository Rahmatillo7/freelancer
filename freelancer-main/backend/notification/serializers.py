from rest_framework import serializers

from backend.notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['user', 'type', 'message', 'read_status', 'timestamp']