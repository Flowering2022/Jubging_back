from django.contrib import admin

from plogging.models import PloggingLog
from .models import User

admin.site.register(User)
admin.site.register(PloggingLog)
