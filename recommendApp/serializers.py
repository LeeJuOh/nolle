from rest_framework import serializers
from loginApp.serializers import UserSerializer
from .models import *
from django.db.models import Avg, Max, Min, Sum

class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = ('place_id', 'place_name')

class UserPlaceHistoryDetailSerializer(serializers.ModelSerializer):

    nickname = serializers.CharField(required=False, source='user_idx.nickname')
    image = serializers.ImageField(required=False, source='user_idx.image')
    class Meta:
        model = UserPlaceHistory
        fields = ('idx','image', 'place_id', 'context', 'img_url_1', 'img_url_2', 'img_url_3', 'img_url_4', 'img_url_5', 'date', 'tag_1', 'tag_2', 'tag_3', 'tag_4', 'tag_5', 'tag_6', 'place_name', 'user_idx', 'nickname', 'rating','like_cnt')


class RecommendSerializer(serializers.ModelSerializer) :

    place = UserPlaceHistorySerializer(source='userplacehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'nickname', 'place')

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'