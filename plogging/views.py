from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from plogging.models import PloggingLog


class PloggingLogAPI(APIView):
    def get(self, request, pk):
        queryset = PloggingLog.objects.filter(userid=pk)
        user_plogging_freq = queryset.count()
        user_totals = queryset.aggregate(Sum('distance'))
        user_totals['plogging_freq'] = user_plogging_freq

        return Response(user_totals)
        # user_total_distance = queryset.aggregate(Sum('distance'))
        #
        # return Response({"totals": user_total_distance, "user_plogging_freq": user_plogging_freq})


