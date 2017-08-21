"""IL3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from main import views

from authentication.views import signin

from authentication.views import web_signout
from authentication.views import web_signin
from authentication.views import web_register
from authentication.views import web_profile

from web.views import home
from web.views import admin_addlock

from web.views import web_lock
from web.views import web_unlock
from web.views import web_logs
from web.views import web_add_user

urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^admin/', admin.site.urls),

    url(r'^mcu/lock/(?P<mac>[-\w]+)$', views.lock, name='lock'),
    url(r'^mcu/unlock/(?P<mac>[-\w]+)$', views.unlock, name='unlock'),
    url(r'^mcu/state/(?P<mac>[-\w]+)$', views.state, name='state'),

    url(r'^login/(?P<username>[-\w]+)/(?P<password>[-\w]+)$', signin, name='signin'),
    url(r'^authentication/logout/$', web_signout, name='web_signout'),
    url(r'^authentication/login/$', web_signin, name='web_signin'),
    url(r'^authentication/register/$', web_register, name='web_register'),
    url(r'^authentication/profile/$', web_profile, name='web_profile'),

    url(r'^web/lock/(?P<mac>[-\w]+)$', web_lock, name='web_lock'),
    url(r'^web/unlock/(?P<mac>[-\w]+)$', web_unlock, name='web_unlock'),
    url(r'^web/logs/(?P<mac>[-\w]+)$', web_logs, name='web_logs'),
    url(r'^web/adduser/(?P<mac>[-\w]+)$', web_add_user, name='web_add_user'),

    url(r'^admin/addlock/$', admin_addlock, name='admin_addlock'),
]
