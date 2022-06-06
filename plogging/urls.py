from django.urls import path

from plogging.views import PloggingLogAPI

urlpatterns = [
    path('<int:pk>', PloggingLogAPI.as_view()),
]