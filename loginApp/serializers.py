from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('idx', 'nickname', 'user_email', 'password', 'user_nm', 'age', 'sex')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.object.create_user(
            validated_data["nickname"], validated_data["user_email"], validated_data["user_nm"], validated_data["age"], validated_data["sex"], validated_data["password"],

        )
        return user

# user 확인용
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

