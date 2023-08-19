from rest_framework import serializers
from bookmarkedapi.models import Book


class BookSerializer(serializers.ModelSerializer):
    """JSON serializer for books"""
    
    class Meta:
        model = Book
        fields = ('__all__')
