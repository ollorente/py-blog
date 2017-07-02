from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from apps.categoria.models import Tipoacceso, Categoria
from apps.post.models import Post


def indexCategoria(request, u):
	categoria = Categoria.objects.get(slug=u, activo=True, bloqueo=True)
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	post = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:10]
	link = Post.objects.filter(categoria=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'link':link,
	}
	return render(request, 'categoria/index.html', context)