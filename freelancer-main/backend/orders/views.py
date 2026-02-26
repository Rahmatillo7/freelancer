from django.db import models
from rest_framework import generics,permissions,status
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(models.Q(client=user) | models.Q(freelancer=user))

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(models.Q(client=user) | models.Q(freelancer=user))

    def patch(self, request,*args, **kwargs):
        return self.partial_update(request, *args, **kwargs)