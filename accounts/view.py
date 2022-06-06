from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializer import UserGetSerializer, UserPostSerializer
from django.http.response import Http404
from .models import User


class UserAPI(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer = UserGetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404

    # 특정 유저 조회
    # post/{pk}
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserGetSerializer(user)
        return Response(serializer.data)

    # 특정 게시물 수정
    # /post/{pk}
    def post(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserPostSerializer()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

