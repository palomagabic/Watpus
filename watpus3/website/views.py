from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.models import Post, Category


# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, "website/index.html", {'posts':posts})








def registro(request):
    return render(request, "website/registro.html")


