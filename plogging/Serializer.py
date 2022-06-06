from rest_framework import serializers

from plogging.models import PloggingLog


class ploggingGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PloggingLog
        fields = '__all__'
