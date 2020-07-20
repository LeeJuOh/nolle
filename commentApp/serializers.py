from rest_framework import serializers
from .models import *


class PostingReviewSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user_idx.nickname', required=False)

    class Meta:
        model = PostingReviews
        fields = ['idx', 'nickname', 'context', 'date']



class CommentsSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user_idx.nickname', required=False)
    comment = PostingReviewSerializer(source='postingreviews_set', many=True)

    class Meta:
        model = UserPlaceHistory
        fields = ('idx', 'nickname', 'date', 'context', 'comment')

