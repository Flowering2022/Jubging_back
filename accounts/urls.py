from django.urls import path
from accounts.view import UserAPI, UserDetail

urlpatterns = [
    path('', UserAPI.as_view(), name='getUser'),
    path('<int:pk>', UserDetail.as_view())
]
