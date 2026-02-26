from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from backend.orders.models import Order


class Notification(models.Model):

    TYPE_CHOICES = (
        ('orders', 'Order'),
        ('review', 'Review'),
        ('payment', 'Payment'),
        ('message', 'Message'),
        ('system', 'System'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    message = models.TextField()
    read_status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification → {self.user.username} | {self.type}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Notifications"

