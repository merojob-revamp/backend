# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import JobSeeker
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class JobSeekerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = JobSeeker
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        JobSeeker.objects.create(user=user)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')
        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                msg = "Either Username or Password is incorrect."
                raise serializers.ValidationError(msg, code="authorization")
            
        else:
            msg = "Must provide username and password both."
            raise serializers.ValidationError(msg, code="authorization")
        
        data['user'] = user
        return data

class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    def validate(self, data):
        refresh = data.get('refresh')
        try:
            RefreshToken(refresh)
        except TokenError:
            msg = "Invalid token."
            raise serializers.ValidationError(msg, code="authorization")
        
        return data
