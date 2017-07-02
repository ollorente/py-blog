from django.db import models


class Tipoacceso(models.Model):
	tipo = models.CharField(max_length=50)

	def __str__(self):
		return self.tipo

	class Meta:
		ordering = ['tipo']


class Categoria(models.Model):
	titulo = models.CharField(max_length=140)
	slug = models.SlugField(max_length=140)
	menu = models.IntegerField(default=1)
	acceso = models.ForeignKey(Tipoacceso, null=True, blank=True, on_delete=models.CASCADE)
	activo = models.BooleanField(default=True)
	bloqueo = models.BooleanField(default=True)

	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['titulo']