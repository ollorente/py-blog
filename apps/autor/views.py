from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse

from apps.categoria.models import Tipoacceso, Categoria
from apps.post.models import Post


def indexAutor(request, u):
	categoria = User.objects.get(username=u)
	postcount = Post.objects.filter(autor=categoria.id, activo=True, bloqueo=True).count()
	categorias = Categoria.objects.filter(menu=1, activo=True, bloqueo=True).order_by('titulo')
	post = Post.objects.filter(autor=categoria.id, activo=True, bloqueo=True).order_by('-fechacreado')[:10]
	link = Post.objects.filter(autor=categoria.id, activo=True, bloqueo=True).order_by('-vistas')[:10]
	context = {
		'categoria':categoria,
		'categorias':categorias,
		'post':post,
		'postcount':postcount,
		'link':link,
	}
	return render(request, 'autor/index.html', context)