from rest_framework import serializers
from .models import *

class CreatePlaceActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = "idx,"
class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
class UserPickSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPick
        fields = "__all__"

