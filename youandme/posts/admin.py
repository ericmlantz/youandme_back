from django.contrib import admin
from .models import Post, Comment, Like

# Register your models here.

@admin.register(Post) # @admin.register - Registers the models with the admin site
class PostAdmin(admin.ModelAdmin):
    # list_display: Specifies the fields to display in the list view in the admin panel
    list_display = ('id','author','content','created_at','updated_at')
    # search_fields: Adds a search box that searches the specified fields (e.g., usernames, post content).
    
    search_fields = ('author__username','content') # 'author__username' (two underscores between them) means “access the username field of the related User model through the author foreign key.”
    # list_filter: Adds filters in the admin panel sidebar for the specified fields (e.g., creation dates)
    list_filter = ('created_at',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'content','created_at')
    search_fields = ('author__username','content','post__content')
    list_filter = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id','post','author','created_at')
    search_fields = ('author__username', 'post__content')
    list_filter = ('created_at',)
    