from django.contrib import admin
from .models import Requester, Matching
# Register your models here.

admin.site.register(Requester)
admin.site.register(Matching)
