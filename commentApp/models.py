from django.db import models
from loginApp.models import User
from recommendApp.models import UserPlaceHistory

# Create your models here.
class PostingReviews(models.Model):
    idx = models.AutoField(primary_key=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'posting_reviews'
        ordering = ['date']





        