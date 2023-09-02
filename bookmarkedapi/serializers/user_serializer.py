from rest_framework import serializers
from bookmarkedapi.models import User


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'bio',
                  'profile_image_url',
                  'following')


class CreateUserSerializer(serializers.ModelSerializer):
    """JSON serializer to create users"""
    class Meta:
        model = User
        fields = ('__all__')
