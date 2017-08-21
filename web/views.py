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



def home(request):
	if 'username' in request.session:
		sender = []
		for i in Lock.objects.all():
			members = i.member
			for j in json.loads(members):
				if j['user'] == request.user.id:
					sender.append({'mac':i.mac,'name':json.loads(i.state)['name'],'isLock':i.isLock,'active':i.active})
					break
		return render(request,"home.html",{'sender':sender})
	else:
		return render(request,"home-guest.html")

def admin_addlock(request):
	if request.user.is_staff :
		if request.method == 'POST':
			lock = Lock(mac = "FFFFFFFFFF",isLock = False, member = "Hello", state = "hello2",active=timezone.now())
			lock.mac 	= request.POST['mac']
			lock.member = json.dumps([{'user':request.user.id,'rank':1}])
			lock.state	= json.dumps({'name':str(request.POST['name'])})
			lock.active	= timezone.now()
			lock.save()
		sender = []
		for i in Lock.objects.all():
			sender.append({'mac':i.mac,'name':json.loads(i.state)['name'],'isLock':i.isLock,'active':i.active})
		print(sender)
		return render(request,"addlock.html",{'lock':sender})
	return redirect('home')

from enum import Enum
class Action(Enum):
	web_lock = 1
	web_unlock = 2

def web_lock(request,mac):
	locks = Lock.objects.filter(mac=mac)
	if locks:
		for alock in locks:
			members = alock.member
			for j in json.loads(members):
				if j['user'] == request.user.id:
					if alock.isLock == False:
						alock.isLock = True
						alock.save()
						Log.objects.create(lock=alock,user=request.user,action=Action.web_lock.value,date=timezone.now())
					break
	return redirect('home')

def web_unlock(request,mac):
	locks = Lock.objects.filter(mac=mac)
	if locks:
		for alock in locks:
			members = alock.member
			for j in json.loads(members):
				if j['user'] == request.user.id:
					if alock.isLock == True:
						alock.isLock = False
						alock.save()
						Log.objects.create(lock=alock,user=request.user,action=Action.web_unlock.value,date=timezone.now())
					break
	return redirect('home')

def web_logs(request,mac):
	locks = Lock.objects.filter(mac=mac)
	sender = []
	sender_state = {}
	if locks:
		for alock in locks:
			members = alock.member
			for j in json.loads(members):
				if j['user'] == request.user.id:
					users = []
					#print(json.loads(alock.member))
					for u in json.loads(alock.member):
						users.append({'user':User.objects.get(id=u['user']).first_name,'rank':u['rank']})
					sender_state = {'mac':alock.mac,'name':json.loads(alock.state)['name'],'isLock':alock.isLock,'active':alock.active,'member':users}
					for k in Log.objects.filter(lock=alock):
						sender.append({'date':k.date,'action':k.action,'user':k.user})
					break
	return render(request,'logs.html',{'sender':sender,'lock':sender_state})

def web_add_user(request,mac):
	locks = Lock.objects.filter(mac=mac)
	msg = ""
	sender = []
	if locks:
		for alock in locks:
			members = alock.member
			for j in json.loads(members):
				if j['user'] == request.user.id: # check request.user in this lock
					if j['rank'] == 1: # check admin
						if request.method == 'POST' : #method POST
							L = Lock.objects.get(mac=mac)
							L.member = request.POST['detail']
							sender = L.member
							L.save()
						else: # method GET
							L = Lock.objects.get(mac=mac)
							sender = L.member
						return render(request,'add_user.html',{'msg':msg,'sender':sender})
					else:
						return redirect('home')
					break
				else:
					msg = "You are not member of this lock."
	#return render(request,'add_user.html',{'msg':msg,'sender':sender})
	return redirect('home')