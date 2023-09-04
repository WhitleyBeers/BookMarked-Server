from rest_framework import serializers
from bookmarkedapi.models import User, Review


class UserReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for showing user reviews"""
    class Meta:
        model = Review
        fields = ('id',
                  'content',
                  'rating',
                  'user_id',
                  'book_id')
        depth = 1

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'uid',
                  'bio',
                  'profile_image_url',
                  'following')


class CreateUserSerializer(serializers.ModelSerializer):
    """JSON serializer to create users"""
    class Meta:
        model = User
        fields = ('__all__')
