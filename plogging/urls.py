from django.urls import path

from plogging.views import PloggingLogAPI, PloggingLogPostAPI

urlpatterns = [
    path('', PloggingLogPostAPI.as_view()),
    path('<int:pk>', PloggingLogAPI.as_view()),
]