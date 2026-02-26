from rest_framework import serializers

from backend.freelancerprofil.models import FreelancerProfile


class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerProfile
        fields = ['service_type', 'user', 'experience', 'portfolio_link', 'price', 'rating', 'status', 'created', 'updated']