from django.conf.urls import url

from apps.buscar.views import search

urlpatterns = [
	url(r'^$', search, name='vista_buscar'),
]