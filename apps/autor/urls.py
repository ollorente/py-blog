from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from apps.autor.views import indexAutor

urlpatterns = [
	url(r'^$', indexAutor, name='vista_autor'),
]