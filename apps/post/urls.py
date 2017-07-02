from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from apps.post.views import indexPost

urlpatterns = [
	url(r'^$', indexPost, name="vista_post"),
]