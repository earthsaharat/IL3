# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login

isLock = True

def lock(request,mac):
	isLock = True
	return HttpResponse(isLock)

def unlock(request,mac):
	isLock = False
	return HttpResponse(isLock)

def state(request,mac):
	return HttpResponse(isLock)
