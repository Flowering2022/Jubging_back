from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializer import UserGetSerializer, UserPostSerializer
from django.http.response import HttpResponse
from .models import User


def detail(request):
    return HttpResponse("You're looking at question.")

@api_view(['GET'])
def UserGet(request):
    queryset = User.objects.all()
    serializer = UserGetSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def UserPost(request):
    if request.method == 'GET':
        return HttpResponse(status=200)

    if request.method == 'POST':
        serializer = UserPostSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPI(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserGetSerializer(queryset, many=True)
        return Response(serializer.data)
