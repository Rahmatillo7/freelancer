from rest_framework import generics, permissions, filters
from .models import FreelancerProfile
from .serializers import FreelancerProfileSerializer


class FreelancerListAPIView(generics.ListAPIView):
    queryset = FreelancerProfile.objects.filter(status='active')
    serializer_class = FreelancerProfileSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['service_type', 'experience']
    ordering_fields = ['price', 'rating', 'created']


class MyProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = FreelancerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, created = FreelancerProfile.objects.get_or_create(user=self.request.user)
        return profile