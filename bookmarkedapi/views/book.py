from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from bookmarkedapi.serializers import BookSerializer, ReviewSerializer
from bookmarkedapi.models import Book, User, Review

class BookView(ViewSet):
    """Bookedmarked books"""
    def retrieve(self, request, pk):
        """get single book"""
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
        """GET request for a list of books by user"""
        books = Book.objects.all()
        user = request.META['HTTP_AUTHORIZATION']
        books = Book.objects.filter(user_id = user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        """POST request to create a book"""
        user = User.objects.get(id=request.META['HTTP_AUTHORIZATION'])
        book = Book.objects.create(
          user_id = user,
          title = request.data['title'],
          author = request.data['author'],
          description = request.data['description'],
          favorite = request.data['favorite'],
          image_url = request.data['imageUrl'],
          status = request.data['status'],
        )
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """PUT request to update a book"""
        book = Book.objects.get(pk=pk)
        book.title = request.data['title']
        book.author = request.data['author']
        book.description = request.data['description']
        book.favorite = request.data['favorite']
        book.image_url = request.data['imageUrl']
        book.status = request.data['status']
        book.save()
        return Response({'message': 'Book updated successfully'}, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        """DELETE request to delete a book"""
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
      
    @action(methods=['post'], detail=True)
    def post_review(self, request, pk):
        """Post request for a user to leave a review on a book"""
        user_id = User.objects.get(pk=request.META['HTTP_AUTHORIZATION'])
        book_id = Book.objects.get(pk=pk)
        review = Review.objects.create(
            user_id = user_id,
            book_id = book_id,
            content = request.data['content'],
            rating = request.data['rating']
        )
        return Response({'message': 'Review posted'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['get'], detail=True)
    def reviews(self, request, pk):
        """Get request for a user to see reviews on a book"""
        reviews = Review.objects.all()
        reviews = reviews.filter(book_id = pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
