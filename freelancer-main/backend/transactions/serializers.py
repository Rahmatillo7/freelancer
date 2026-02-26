from rest_framework import serializers

from backend.transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'order', 'amount', 'status', 'payment_method', 'timestamp']