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
        fields = ("idx","nickname","image")
class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = "__all__"
class UserLikeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLikeHistory
        fields = "__all__"
class PostingReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostingReviews
        fields = "__all__"
