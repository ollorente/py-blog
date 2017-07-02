from django.contrib import admin

from apps.categoria.models import Tipoacceso, Categoria


admin.site.register(Tipoacceso)
admin.site.register(Categoria)


class TipoaccesoAdmin(admin.ModelAdmin):
	list_display = ('nombre')
	list_display_links = ('nombre')
	class Meta:
		ordering = ('nombre',)


class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('titulo')
	list_display_links = ('titulo')
	class Meta:
		ordering = ('titulo',)