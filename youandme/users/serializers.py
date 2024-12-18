from rest_framework import serializers
from .models import CustomUser

# Serializers define how your models will be converted to JSON for the API.
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','email','bio','profile_picture']