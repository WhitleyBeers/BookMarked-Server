from rest_framework import serializers
from bookmarkedapi.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews"""
    
    class Meta:
        model = Review
        fields = ('__all__')
        depth = 1
