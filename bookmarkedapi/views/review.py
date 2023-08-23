from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bookmarkedapi.serializers import ReviewSerializer
from bookmarkedapi.models import Review


class ReviewView(ViewSet):
    """Bookmarked reviews"""
    def retrieve(self, request, pk):
        """GET single review"""
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        """PUT request to update a review"""
        review = Review.objects.get(pk=pk)
        review.content = request.data['content']
        review.rating = request.data['rating']
        review.save()
        return Response({'message': 'Review updated successfully'}, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        """DELETE request to delete a review"""
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response({'message': 'Review deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
