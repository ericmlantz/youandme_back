from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Cascade means all items post is made up of are deleted as well (i.e: comments, likes) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Like(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # This is a special Django constant that dynamically references the user model being used in the project. By default, this refers to django.contrib.auth.models.User. However, if you’ve defined a custom user model (e.g., CustomUser based on AbstractUser), settings.AUTH_USER_MODEL will point to that instead.
    created_at = models.DateTimeField(auto_now_add=True)