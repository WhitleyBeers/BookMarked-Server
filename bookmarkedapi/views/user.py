from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bookmarkedapi.serializers import UserSerializer, CreateUserSerializer
from bookmarkedapi.models import User


class UserView(ViewSet):
    """Bookmarked API users"""
    def retrieve(self, request, pk):
        """get single user"""
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """GET request for list of users"""
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """PUT request to update a user"""
        user = User.objects.get(pk=pk)
        uid = request.META['HTTP_AUTHORIZATION']
        user.first_name = request.data['firstName']
        user.last_name = request.data['lastName']
        user.bio = request.data['bio']
        user.profile_image_url = request.data['profileImageUrl']
        user.uid = uid
        user.save()
        return Response({'message': 'User updated'}, status=status.HTTP_204_NO_CONTENT)
