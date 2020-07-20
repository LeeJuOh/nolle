from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class UserPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPick
        fields = "__all__"
