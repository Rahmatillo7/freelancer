from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def ger_queryset(self, queryset):
        return Notification.objects.filter(user=self.request.user)

class MarkAsReadView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            notification = Notification.objects.get(pk=pk, users=request.user)
            notification.read = True
            notification.save()
            return Response({"message": "Xabar o'qildi deb belgilandi"}, status=status.HTTP_200_OK)
        except Notification.DoesNotExist:
            return Response({"error": "Bildirishnoma topilmadi"}, status=status.HTTP_404_NOT_FOUND)