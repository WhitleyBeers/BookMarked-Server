from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from bookmarkedapi.serializers import UserSerializer, ReviewSerializer, UserReviewSerializer
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
        pk = request.META['HTTP_AUTHORIZATION']
        follower = User.objects.get(pk=pk)
        users = User.objects.all()
        for user in users:
            user.following = len(Following.objects.filter(
                follower_id = follower,
                author_id = user,
            )) > 0
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """PUT request to update a user"""
        user = User.objects.get(pk=pk)
        user.first_name = request.data['firstName']
        user.last_name = request.data['lastName']
        user.bio = request.data['bio']
        user.profile_image_url = request.data['profileImageUrl']
        user.email = request.data['email']
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
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['get'], detail=True)
    def checkfollowing(self, request, pk):
        """Checks to see if a user is following another user"""
        user = User.objects.get(pk=pk)
        follower = request.META['HTTP_AUTHORIZATION']
        follower = User.objects.get(id=follower)
        user.following = len(Following.objects.filter(
            follower_id = follower,
            author_id = pk,
        )) > 0
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=True)
    def following(self, request, pk):
        """Gets users that a specific user follows"""
        user = User.objects.get(pk=pk)
        following_list = Following.objects.filter(follower_id=user)
        reviews = []
        for following in following_list:
            author=following.author_id
            author_reviews=Review.objects.filter(user_id=author)
            reviews.extend(author_reviews)
        serializer = UserReviewSerializer(reviews, many=True)
        return Response(serializer.data)
