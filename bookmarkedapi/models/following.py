from django.db import models
from .user import User

class Following(models.Model):
    """Model for following users"""
    
    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
