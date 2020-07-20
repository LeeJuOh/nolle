from rest_framework import serializers
# from .models import UserPick
from recommendApp.models import *
from pick.models import UserPick
from .models import UserSearchHistory


class UserSearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSearchHistory
        fields = '__all__'

class RecommendUserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = ['place_id', 'place_name']

class UserPlaceHistorySerializer(serializers.ModelSerializer):

    nickname = serializers.CharField(required=False, source='user_idx.nickname')
    image = serializers.ImageField(required=False, source='user_idx.image')
    class Meta:
        model = UserPlaceHistory
        fields = ('idx','image', 'place_id', 'context', 'img_url_1', 'img_url_2', 'img_url_3', 'img_url_4', 'img_url_5', 'date', 'tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5', 'tag_6', 'place_name', 'user_idx', 'nickname', 'rating')


class PickPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPick
        fields = '__all__'


class CategoryImageMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImageM
        fields = '__all__'


class CategoryImageSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImageS
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer) :

    recommend_place = RecommendUserPlaceHistorySerializer(source='userplacehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'nickname', 'image','recommend_place',)