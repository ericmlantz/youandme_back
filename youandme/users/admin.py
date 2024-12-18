from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser) # @admin.register - Registers the models with the admin site
class CustomUserAdmin(admin.ModelAdmin):
    # list_display: Specifies the fields to display in the list view in the admin panel
    list_display = ('id','username','first_name','last_name','email','profile_picture')
    # search_fields: Adds a search box that searches the specified fields (e.g., usernames, post content).
    search_fields = ('username',) # 'author__username' (two underscores between them) means “access the username field of the related User model through the author foreign key.”
    # list_filter: Adds filters in the admin panel sidebar for the specified fields (e.g., creation dates)
    list_filter = ('first_name', 'last_name',)
    #ordering: Sets the default ordering in the admin view
    ordering = ('id',)