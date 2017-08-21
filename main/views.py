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

def lock(request,mac):
	lock = Lock.objects.get(mac=mac)
	if lock.isLock == False:
		lock.isLock = True
		lock.save()
		Log.objects.create(lock=lock,user=User.objects.get(username="unknow"),action=3,date=timezone.now())
	return HttpResponse(lock.isLock)

def unlock(request,mac):
	lock = Lock.objects.get(mac=mac)
	if lock.isLock == True:
		lock.isLock = False
		lock.save()
		Log.objects.create(lock=lock,user=User.objects.get(username="unknow"),action=4,date=timezone.now())
	return HttpResponse(lock.isLock)

def state(request,mac):
	isLock = Lock.objects.get(mac=mac).isLock
	return HttpResponse(isLock)
