from django.db import models


class User(models.Model):
    """User model"""
    
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    uid = models.CharField(max_length=50)
    bio = models.CharField(max_length=254)
    profile_image_url = models.URLField(max_length=254)
    
    @property
    def following(self):
        return self.__following
    
    @following.setter
    def following(self, value):
        self.__following = value
