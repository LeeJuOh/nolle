from loginApp.models import User
from rest_framework import serializers
from .models import *


class PostFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = '__all__'


class UserFollowSerializer (serializers.ModelSerializer) :
    follow_nickname = serializers.CharField(source='following_idx.nickname', required=False)
    follow_name = serializers.CharField(source='following_idx.user_nm', required=False)
    follow_email = serializers.CharField(source='following_idx.user_email', required=False)
    follow_image = serializers.ImageField(source='following_idx.image', required=False)

    class Meta:
        model = UserFollow
        fields = ['following_idx', 'follow_nickname', 'follow_name', 'follow_email', 'follow_image']

class UserFollowerSerializer (serializers.ModelSerializer) :
    follower_nickname = serializers.CharField(source='user_idx.nickname', required=False)
    follower_name = serializers.CharField(source='user_idx.user_nm', required=False)
    follower_email = serializers.CharField(source='user_idx.user_email', required=False)
    follower_image = serializers.ImageField(source='user_idx.image', required=False)

    class Meta:
        model = UserFollow
        fields = ['user_idx', 'follower_nickname', 'follower_name', 'follower_email', 'follower_image']


class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = '__all__'
        read_only_fields = ('idx',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['idx', "nickname", 'image',"sex", 'age', 'description']


class UserLikeSerializer(serializers.ModelSerializer):

    posting = UserPlaceHistorySerializer(source='posting_idx')
    class Meta:
        model = UserLikeHistory
        fields = [ 'posting']
        read_only_fields = ('idx',)


class MyPageSerializer(serializers.ModelSerializer):

    like_history = UserLikeSerializer(source='mypage_userlikehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', "nickname", 'user_nm', 'image', "sex", 'age', 'description', 'posting_cnt', 'following_cnt', 'follower_cnt',  'like_history')
        read_only_fields = ('idx',)


class UserPageSerializer(serializers.ModelSerializer):

    my_posting = UserPlaceHistorySerializer(source='userplacehistory_set', many=True)
    like_history = UserLikeSerializer(source='mypage_userlikehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'nickname', 'image', "sex", 'age', 'description', 'posting_cnt', 'following_cnt', 'follower_cnt', 'my_posting', 'like_history')
        read_only_fields = ('idx',)


class UserFollowSerializer(serializers.ModelSerializer):

    follow_list = UserFollowSerializer(source='user_idx', many=True)
    follower_list = UserFollowerSerializer(source='following_idx', many=True)

    class Meta:
        model = User
        fields = ['idx', 'nickname', 'user_email', 'image','follow_list', 'follower_list' ]




