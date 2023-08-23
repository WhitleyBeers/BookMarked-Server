from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from bookmarkedapi.serializers import UserSerializer, ReviewSerializer
from bookmarkedapi.models import User, Review, Following


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

    @action(methods=['get'], detail=True)
    def reviews(self, request, pk):
        """Get request to see reviews a specific user has left"""
        reviews = Review.objects.all()
        reviews = reviews.filter(user_id = pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def follow(self, request, pk):
        """Post request for a user to follow another user"""
        follower_id = User.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        author_id = User.objects.get(pk=pk)
        following = Following.objects.create(
            follower_id=follower_id,
            author_id=author_id
        )
        return Response({'message': 'Now following user'}, status=status.HTTP_201_CREATED)

    @action(methods=['delete'], detail=True)
    def unfollow(self, request, pk):
        """Delete request for a user to unfollow another user"""
        follower_id = User.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        author_id = User.objects.get(pk=pk)
        following = Following.objects.get(
            follower_id=follower_id,
            author_id=author_id
        )
        following.delete()
        return Response({'message': 'User unfollowed'}, status=status.HTTP_204_NO_CONTENT)
