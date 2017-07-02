"""py-blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an iport:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include('apps.home.urls')),

	url(r'^buscar/', include('apps.buscar.urls'), name='buscar'),
	url(r'^autor/(?P<u>[\w-]+)/$', include('apps.autor.urls'), name='autor'),
	url(r'^(?P<u>[\w-]+)/$', include('apps.categoria.urls'), name='categoria'),
	url(r'^(?P<u>[\w-]+)/(?P<v>\d+)/(?P<w>[\w-]+)/$', include('apps.post.urls'), name='post'),
]
