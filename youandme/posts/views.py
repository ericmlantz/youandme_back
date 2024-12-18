from .models import Post, Comment, Like
from rest_framework import viewsets 
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.permissions import AllowAny # This will temporarily allow anyone to access the /api/posts/ endpoint without authentication. Put in the ViewSet below that you want to apply it to.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission


# Create your views here.

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


# ModelViewSet is a built-in DRF class that provides a full set of views for a model. 
# It handles all basic API operations (list, retrieve, create, update, and delete) out of the box.
# It uses the queryset to determine what data to operate on.
# It uses the serializer_class to determine how the data should be validated and serialized for API responses
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthor, IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author','created_at']
    
    # Sets the author field automatically based on the authenticated user making the request.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer