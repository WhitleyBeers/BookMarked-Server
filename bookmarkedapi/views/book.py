from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from bookmarkedapi.serializers import BookSerializer
from bookmarkedapi.models import Book

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
