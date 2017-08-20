# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

class Lock(models.Model):
    mac 	= models.CharField(max_length=11)
    member 	= models.TextField()
    state	= models.TextField()
    isLock	= models.BooleanField()
    active	= models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        return self.mac

class Log(models.Model):
	lock 	= models.ForeignKey(Lock)
	user	= models.ForeignKey('auth.User')
	action	= models.IntegerField()
	date 	= models.DateTimeField(default=timezone.now)