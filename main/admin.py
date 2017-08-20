# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Lock
from .models import Log

admin.site.register(Lock)
admin.site.register(Log)