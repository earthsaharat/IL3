# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.utils import timezone

from main.models import Lock
from main.models import Log

def open(request,mac,side):
	lock = Lock.objects.get(mac=mac)
	Log.objects.create(lock=lock,user=User.objects.get(username="unknow"),action=3+int(side),date=timezone.now())
	return HttpResponse(lock.isLock)
 

def state(request,mac):
	isLock = Lock.objects.get(mac=mac).isLock
	return HttpResponse(isLock)
