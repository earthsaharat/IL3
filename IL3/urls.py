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
from authentication.views import login
from authentication.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/$', views.test, name='test'),
    url(r'^lock/$', views.lock, name='lock'),
    url(r'^unlock/$', views.unlock, name='unlock'),
    url(r'^state/$', views.state, name='state'),

    url(r'^login/(?P<username>[-\w]+)/(?P<password>[-\w]+)$', login, name='login'),
]
