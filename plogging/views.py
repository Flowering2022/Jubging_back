from django.db.models import Sum
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from plogging.models import PloggingLog


class PloggingLogAPI(APIView):
    def get(self, request, pk):
        queryset = PloggingLog.objects.filter(userid=pk)
        user_total_distance = queryset.aggregate(Sum('distance'))
        return Response(user_total_distance)
