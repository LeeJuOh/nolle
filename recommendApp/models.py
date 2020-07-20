from django.db import models
from loginApp.models import User
import os
from uuid import uuid4
from django.utils import timezone
from follow_feed.models import date_upload_posting
# Create your models here.
from follow_feed.models import UserLikeHistory
from pick.models import UserPick



class CategoryL(models.Model):
    ctgr_lid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'category_l'


class CategoryImageM(models.Model):
    ctgr_mid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45)
    large = models.ForeignKey(CategoryL, models.DO_NOTHING, blank=True, null=True,
                              related_name="recommend_categoryimagem_large")

    class Meta:
        managed = False
        db_table = 'category_image_m'


class CategoryImageS(models.Model):
    ctgr_sid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    large = models.ForeignKey(CategoryImageM, models.DO_NOTHING, blank=True, null=True,
                              related_name="recommend_categoryimages_large")
    middle = models.ForeignKey(CategoryImageM, models.DO_NOTHING, blank=True, null=True,
                               related_name="recommend_categoryimages_middle")
    ctgr_name_en = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_image_s'
        unique_together = (('ctgr_name', 'middle'),)


class CategoryTextM(models.Model):
    ctgr_id = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    large = models.ForeignKey(CategoryL, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_text_m'


class CategoryTextS(models.Model):
    ctgr_id = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    middle = models.ForeignKey(CategoryTextM, models.DO_NOTHING, blank=True, null=True)
    large = models.ForeignKey(CategoryL, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_text_s'

class UserPlaceHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    place_id = models.CharField(max_length=100, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    img_url_1 = models.ImageField(upload_to=date_upload_posting, null=True, blank=True)
    img_url_2 = models.ImageField(upload_to=date_upload_posting, null=True, blank=True)
    img_url_3 = models.ImageField(upload_to=date_upload_posting, null=True, blank=True)
    img_url_4 = models.ImageField(upload_to=date_upload_posting, null=True, blank=True)
    img_url_5 = models.ImageField(upload_to=date_upload_posting, null=True, blank=True)
    like_cnt = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    tag_1 = models.CharField(max_length=45, blank=True, null=True)
    tag_2 = models.CharField(max_length=45, blank=True, null=True)
    tag_3 = models.CharField(max_length=45, blank=True, null=True)
    tag_4 = models.CharField(max_length=45, blank=True, null=True)
    tag_5 = models.CharField(max_length=45, blank=True, null=True)
    tag_6 = models.CharField(max_length=45, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    place_name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_place_history'



class UserLScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    ctgr_idx = models.ForeignKey(CategoryL, models.DO_NOTHING, db_column='ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_l_score'


class UserLHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryL, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user_l_history'


class ImageMHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryImageM, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'image_m_history'


class ImageSHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryImageS, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'image_s_history'


class TextMHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryTextM, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'text_m_history'


class TextSHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryTextS, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'text_s_history'


class TextMScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    text_ctgr_idx = models.ForeignKey(CategoryTextM, models.DO_NOTHING, db_column='text_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'text_m_score'


class TextSScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    text_ctgr_idx = models.ForeignKey(CategoryTextS, models.DO_NOTHING, db_column='text_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'text_s_score'


class ImageMScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    image_ctgr_idx = models.ForeignKey(CategoryImageM, models.DO_NOTHING, db_column='image_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'image_m_score'


class ImageSScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    image_ctgr_idx = models.ForeignKey(CategoryImageS, models.DO_NOTHING, db_column='image_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True,
                                    null=True)

    class Meta:
        managed = False
        db_table = 'image_s_score'

def date_upload_recommend(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    # 길이 32 인 uuid 값
    uuid_name = uuid4().hex
    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    # 결합 후 return
    return '/'.join([
        'recommend',
        ymd_path,
        uuid_name + extension,
        ])

class Upload(models.Model):
    image = models.ImageField(upload_to=date_upload_recommend)

    class Meta:
        db_table = 'upload'
