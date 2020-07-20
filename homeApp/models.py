from django.db import models
from loginApp.models import User
from recommendApp.models import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

def date_upload_profile(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    # 길이 32 인 uuid 값
    uuid_name = uuid4().hex
    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    # 결합 후 return
    return '/'.join([
        'profile',
        ymd_path,
        uuid_name + extension,
        ])


# class UserManager(BaseUserManager):
#     def create_user(self, user_id, user_email, password=None):
#         if not user_email:
#             raise ValueError("Users must have an email address")
#
#         user = self.model(
#             user_id=user_id,
#             user_email=self.normalize_email(user_email)
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, user_id, user_email, password=None):
#         user = self.create_user(
#             user_id=user_id,
#             user_email=self.normalize_email(user_email),
#             password=password
#
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
#
# class User(AbstractBaseUser):
#
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     idx = models.AutoField(primary_key=True)
#     nickname = models.CharField(unique=True,max_length=100, null = True)
#     user_nm = models.CharField(max_length=50, null = True)
#     user_email = models.CharField(unique=True, max_length=100, null = True)
#     posting_cnt = models.IntegerField(blank=True, null=True, default = 0)
#     following_cnt = models.IntegerField(blank=True, null=True, default = 0)
#     follower_cnt = models.IntegerField(blank=True, null=True, default = 0)
#     description = models.TextField(blank=True, null=True)
#     age = models.DateField(blank=True,null = True)
#     sex = models.CharField(max_length=45, blank=True,null = True)
#     image = models.ImageField(upload_to=date_upload_profile, default='default/default.png')
#
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#
#     object = UserManager()
#     USERNAME_FIELD = 'user_email'
#     # REQUIRED_FIELDS = ['user_id']
#
#     class Meta:
#         managed = False
#         db_table = 'user'

# Create your models here.
class UserSearchHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_search_history'

class UserPick(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True, related_name = 'home_userpick_set')
    place_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pick'
        unique_together = (('user_idx', 'place_id'),)
