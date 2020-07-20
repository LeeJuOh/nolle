from django.db import models
from loginApp.models import User
from recommendApp.models import UserPlaceHistory
# Create your models here.
class UserLikeHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True, related_name = 'mypage_userlikehistory_set')

    class Meta:
        managed = False
        db_table = 'user_like_history'
        unique_together = (('posting_idx', 'user_idx'),)


class UserFollow(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING,related_name='user_idx', db_column='user_idx')
    following_idx = models.ForeignKey(User, models.DO_NOTHING,related_name='following_idx', db_column='following_idx')

    class Meta:
        managed = False
        db_table = 'user_follow'
        unique_together = (('user_idx', 'following_idx'),)