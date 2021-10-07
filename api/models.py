import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    pass

class StageData(models.Model):
    id = models.AutoField(help_text="Stage ID", primary_key=True)
    stageTitle = models.CharField(max_length=200)
    stageImglink = models.CharField(max_length=200)

    class Meta:
        db_table = 'StageData'

class Review(models.Model):
    id = models.AutoField(help_text="Review ID", primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user", on_delete=models.CASCADE, db_column="user_id")
    stage_id = models.ForeignKey("StageData", related_name="stage", on_delete=models.CASCADE, db_column="stage_id")
    reviewContents = models.CharField(max_length=2000)
    point = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)