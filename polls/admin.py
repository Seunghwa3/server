from django.contrib import admin
from .models import Receive, Send

# Register your models here.

admin.site.register(Receive)
admin.site.register(Send)