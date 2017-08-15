# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from django.http import JsonResponse
import json

from django.contrib.auth import authenticate, login


# Create your views here.
def test(request):
	#return JsonResponse({'a':"Hello"})
	return HttpResponse("Hello")
