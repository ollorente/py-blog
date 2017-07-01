from django.shortcuts import render
from django.http import HttpResponse


def indexHome(request):
	return render(request, 'home/index.html')