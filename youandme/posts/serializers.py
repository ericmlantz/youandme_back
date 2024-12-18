from rest_framework import serializers
from .models import Post, Comment, Like

 # serializers ensures that API responses and requests are serialized (converted to/from JSON).
class PostSerializer(serializers.ModelSerializer):
    
    #The author field links to the user who created the post. When serialized using StringRelatedField, 
    # it outputs the value of the __str__() method defined in the user model. 
    # By default,Django’s User model defines __str__() to return the username.
    author = serializers.StringRelatedField() # Use StringRelatedField when you only need a string representation of the related object, to avoid embedding the entire related object or its ID.
    
    
    class Meta:
        model = Post
        fields = ['id','author','content','created_at','updated_at']
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Comment
        fields = ['id','post','author','content','created_at']

class LikeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    
    class Meta:
        model = Like
        fields = ['id','post','author','created_at']
    