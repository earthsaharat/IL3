# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def login(request,username,password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        #login(request, user)
        # Redirect to a success page.
        return HttpResponse("C")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("E")

 def logout(request):
 	logout(request)
 	return HttpResponse("C")

@csrf_exempt
def login2(request):
	if request.method == 'GET':
		return JsonResponse({'key': 'get'})
	if request.method == 'POST':
		d = json.loads(request.body)
		print(d.get("username","ERROR"))
		print(d.get("password","ERROR"))
		return JsonResponse({'key': 'post'})