from rest_framework import serializers

from plogging.models import PloggingLog


class ploggingGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PloggingLog
        fields = '__all__'


class ploggingPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PloggingLog
        fields = ['userid', 'distance', 'runningtime']
