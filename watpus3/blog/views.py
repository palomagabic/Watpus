from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.
def blog(request):
    posts = Post.objects.all()

    page = request.GET.get('page',1)
    paginator = Paginator(posts,1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/blog.html",{'posts':posts})

def category(request, category_id):
    category = get_object_or_404(Category, id = category_id)
    return render(request, "blog/category.html", {'category':category})

def post(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "blog/post.html", {'post':post,
                                            'comments':comments,
                                            'new_comment':new_comment,
                                            'comment_form':comment_form})
