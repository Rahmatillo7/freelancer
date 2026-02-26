from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from backend.orders.models import Order


class Transaction(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    )

    PAYMENT_METHOD_CHOICES = (
        ('card', 'Card'),
        ('paypal', 'PayPal'),
        ('click', 'Click'),
        ('payme', 'Payme'),
        ('cash', 'Cash'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transactions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction #{self.id} | {self.user.username} | {self.amount}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Transactions"