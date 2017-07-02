from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q

from apps.categoria.models import Tipoacceso, Categoria
from apps.post.models import Post


def search(request):
	query = request.GET.get('q', '')
	if query:
		qset = (
			Q(titulo__icontains=query) |
			Q(categoria__icontains=query) |
			Q(contenido__icontains=query) |
			Q(autor__icontains=query)
		)
		results = Post.objects.filter(qset).distinct()
	else:
		results = []
	context = {'results':results, 'query':query}
	return render(request, 'buscar/index.html', context)