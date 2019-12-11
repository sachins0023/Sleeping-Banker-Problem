from rest_framework import serializers
from .models import User, Session

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'mobile_number', 'user_name', 'headers')
        
# class UserCreateSerializer(serializers.ModelSerializer):

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'session_key', 'user', 'user_agent', 'ip_address', 'active')