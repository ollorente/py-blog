from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from apps.home.views import indexHome

urlpatterns = [
	url(r'^$', indexHome, name="vista_home"),
]