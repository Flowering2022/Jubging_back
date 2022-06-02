from rest_framework import serializers
from .models import User


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'kakao_id', 'total_distance']


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username', 'kakao_id']
