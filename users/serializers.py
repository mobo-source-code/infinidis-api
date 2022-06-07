from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework.authtoken.models import Token

from users.models import CustomUser
from dj_rest_auth.models import TokenModel

class ToRegisterSerializer(RegisterSerializer):
    username = None

class ToLoginSerializer(LoginSerializer):
    username = None

class UserSerializer(serializers.ModelSerializer):
    username = None
    class Meta: 
        model = CustomUser
        fields ='__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = TokenModel
        fields = ('key', 'user')
