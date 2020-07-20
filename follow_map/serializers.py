from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("idx","nickname","image")
class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = "__all__"

class UserLScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLScore
        fields = "__all__"
class ImageMScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageMScore
        fields = "__all__"

class ImageSScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSScore
        fields = "__all__"
class TextMScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextMScore
        fields = "__all__"
class TextSScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextSScore
        fields = "__all__"


