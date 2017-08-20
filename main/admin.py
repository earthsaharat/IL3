# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Lock
from .models import Log


class LockAdmin(admin.ModelAdmin):
    list_display = ('mac', 'member', 'state','isLock','active')
admin.site.register(Lock,LockAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display = ('lock', 'user', 'action','date')
admin.site.register(Log,LogAdmin)
