from django.contrib import admin
from .models import Category, Comment, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post__categories')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'

    def post__categories(self,cat):
        return ", ".join([c.name for c in cat.categories.all()])
    post__categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)