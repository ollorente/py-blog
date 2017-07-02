from django.contrib import admin

from apps.post.models import Post


admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'slug')
	search_field = ('titulo',)
	list_display_links = ('titulo')
	prepopulated_fields = {'slug': ('titulo',)}

	class Meta:
		ordering = ('titulo',)