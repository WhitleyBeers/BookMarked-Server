from rest_framework import serializers
from bookmarkedapi.models import User


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users"""
    class Meta:
        model = User
        fields = ('__all__')


class CreateUserSerializer(serializers.ModelSerializer):
    """JSON serializer to create users"""
    class Meta:
        model = User
        fields = ('__all__')
