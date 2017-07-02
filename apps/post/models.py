from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from apps.categoria.models import Tipoacceso, Categoria


class Post(models.Model):
	titulo = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140, unique=True)
	categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
	contenido = models.TextField()
	autor = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	fechacreado = models.DateTimeField(auto_now_add=True, blank=True)
	fechainicio = models.DateTimeField(blank=True)
	fechafinal = models.DateTimeField(blank=True)
	fechamodificado = models.DateTimeField(auto_now_add=True, blank=True)
	acceso = models.ForeignKey(Tipoacceso, null=True, blank=True, on_delete=models.CASCADE)
	tags = models.TextField(null=True, blank=True)
	vistas = models.IntegerField(null=True, blank=True)
	activo = models.BooleanField(default=True)
	bloqueo = models.BooleanField(default=True)

	def slug(self):
		return slugify(self.titulo)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['titulo']