from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="Titulo", max_length=100)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edicion")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name 

class Post(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="post")
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha edicion")

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        ordering = ['-created']

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text