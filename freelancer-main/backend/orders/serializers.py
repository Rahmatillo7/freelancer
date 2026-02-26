from rest_framework import serializers

from backend.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['client', 'freelancer', 'service_type', 'date_time', 'price', 'status', 'payment_status', 'created', 'updated']