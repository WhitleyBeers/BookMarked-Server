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
