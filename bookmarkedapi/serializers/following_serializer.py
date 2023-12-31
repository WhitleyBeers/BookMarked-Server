from rest_framework import serializers
from bookmarkedapi.models import Following


class FollowingSerializer(serializers.ModelSerializer):
    """JSON serializer for following list"""
    class Meta:
        model = Following
        fields = ('author_id',
                  'reviews')
        depth = 1
