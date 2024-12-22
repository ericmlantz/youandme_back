from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, BasePermission
# from rest_framework.permissions import AllowAny   # This will temporarily allow anyone to access the /api/posts/ endpoint without authentication. Put in the ViewSet below that you want to apply it to.


# Additional Options

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class CustomPagination(PageNumberPagination):
    page_size = 10

# Create your views here.

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
    pagination_class = CustomPagination
    
    # Sets the author field automatically based on the authenticated user making the request.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author','created_at']
    pagination_class = CustomPagination
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthor()]  # Custom permission to check if the user is the author
        return super().get_permissions()
    
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author','created_at']
    
    # Ensure only the like author can delete their like
    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAuthor()]  # Custom permission to check if the user is the author
        return super().get_permissions()