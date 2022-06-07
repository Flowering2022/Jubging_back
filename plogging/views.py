from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from plogging.Serializer import ploggingPostSerializer
from plogging.models import PloggingLog


class PloggingLogPostAPI(APIView):
    def post(self, request):
        serializer = ploggingPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PloggingLogAPI(APIView):
    def get(self, request, pk):
        queryset = PloggingLog.objects.filter(userid=pk)
        user_plogging_freq = queryset.count()
        user_totals = queryset.aggregate(Sum('distance'))
        user_totals['plogging_freq'] = user_plogging_freq

        return Response(user_totals)

