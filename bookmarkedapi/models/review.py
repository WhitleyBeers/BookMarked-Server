from django.db import models
from .book import Book
from .user import User


class Review(models.Model):
    """review model"""
    
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.CharField(max_length=254)
    rating = models.IntegerField()
