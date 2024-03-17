from django.shortcuts import render, get_object_or_404
from .models import Post

def index_view(request):
    posts = Post.objects.all().order_by('-created_at')[:3]
    return render(request, 'index.html',{'posts': posts})

def posts_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts.html',{'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})
