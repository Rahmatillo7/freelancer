from rest_framework import serializers

from backend.review.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['order', 'client', 'freelancer', 'rating', 'comment', 'verified', 'created', 'updated']