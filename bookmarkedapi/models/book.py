from django.db import models
from .user import User


class Book(models.Model):
    """Book model"""
    
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    favorite = models.BooleanField(default=False)
    image_url = models.URLField(max_length=254)
    status = models.CharField(max_length=254)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    date_added = models.DateField(auto_now_add=True)
