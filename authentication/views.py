# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse

from django.contrib.auth import authenticate, login, update_session_auth_hash,logout
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def signin(request,username,password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        #login(request, user)
        # Redirect to a success page.
        return HttpResponse("C")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("E")

def web_signout(request):
	if 'username' in request.session:
		del request.session['username']
		#print "del uname"
	logout(request)
	return redirect('home')

import sys
def web_signin(request):
	if request.method == 'POST' and 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		#print >>sys.stderr, "debug"
		if user is not None:
			if user.is_active:
				if 'remember' in request.POST:
					#print>>sys.stderr, "%s type: %s"%(request.POST['remember'],type(request.POST['remember']))
					if request.POST['remember']=='1':
						request.session.set_expiry(604800) #remember keep session for a week
				else:
					request.session.set_expiry(14400) #not remember keep session for 4hrs
				#print >>sys.stderr, "session expiry: %s"%request.session.get_expiry_age()

				login(request, user)
				#if 'username' in request.session:
					#print >>sys.stderr, "username_i: %s"%request.session['username']
				request.session['username'] = user.username
				#print >>sys.stderr, "username_f: %s"%request.session['username']
				
				return redirect('home')
			else:
				msg="Disabled account"
		else:
			msg="Invalid username or password"
		return render(request,'login.html',{'msg': msg})   
	return render(request,'login.html',{'msg': ""})

def web_register(request):
	msg = ""
	if request.method == 'POST':
		username 	= request.POST['username']
		password 	= request.POST['password']
		passwordc 	= request.POST['password-c']
		name		= request.POST['first_name']
		if password == passwordc :
			if not User.objects.filter(username=username):
				user = User.objects.create_user(username, None, password)
				user.first_name = name
				user.save()
				login(request, user)
				return redirect('home')
			else:
				msg = "A user with that username already exists."
		else:
			msg = "The two password fields didn't match."
	return render(request,'register.html',{'msg': msg})

#@csrf_exempt
#def login2(request):
#	if request.method == 'GET':
#		return JsonResponse({'key': 'get'})
#	if request.method == 'POST':
#		d = json.loads(request.body)
#		print(d.get("username","ERROR"))
#		print(d.get("password","ERROR"))
#		return JsonResponse({'key': 'post'})

def web_profile(request):
	if request.method == 'POST' and request.user.is_authenticated:
		user = User.objects.get(id=request.user.id)
		user.first_name = request.POST['first_name']
		user.save()
		return redirect('home')
	sender = {'username':request.user.username,'name':request.user.first_name,'id':request.user.id}
	return render(request,'profile.html',{'sender':sender})