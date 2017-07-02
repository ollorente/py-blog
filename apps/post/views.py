from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from apps.categoria.models import Tipoacceso, Categoria
from apps.post.models import Post


def indexPost(request, u, v, w):
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	post = Post.objects.filter(id=v, activo=True, bloqueo=True)
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'link':link,
	}
	return render(request, 'post/index.html', context)