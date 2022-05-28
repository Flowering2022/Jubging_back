from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    kakao_id = models.CharField(max_length=50)
    total_distance = models.IntegerField(default=0)
