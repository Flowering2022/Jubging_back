from django.urls import path
from accounts.view import UserAPI

urlpatterns = [
    path('get/', UserAPI.as_view() , name='getUser'),
    # path('post/', accounts.view.UserPost),
]
