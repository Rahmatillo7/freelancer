from django.urls import path
from .views import FreelancerListAPIView, MyProfileAPIView

urlpatterns = [
    path('all/', FreelancerListAPIView.as_view(), name='freelancer-list'),
    path('me/', MyProfileAPIView.as_view(), name='my-freelancer-profile'),
]