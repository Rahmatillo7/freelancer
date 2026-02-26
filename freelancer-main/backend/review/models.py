from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from backend.orders.models import Order


class Review(models.Model):

    RATING_CHOICES = (
        (1, '1 - Very Bad'),
        (2, '2 - Bad'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='review')
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client_reviews')
    freelancer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='freelancer_reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review #{self.id} - Order #{self.order.id} | Rating: {self.rating}"

    class Meta:
        verbose_name_plural = "Reviews"