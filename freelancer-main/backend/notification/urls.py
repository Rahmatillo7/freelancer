from django.urls import path
from .views import NotificationListView,MarkAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='order-list'),
    path('<int:pk>/', MarkAsReadView.as_view(), name='mark-as-read'),
]