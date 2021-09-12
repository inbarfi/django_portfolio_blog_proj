from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .models import Post
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request, 'home.html')#context

def about(request):
    return render(request, 'about.html')

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts':posts})
#.all

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else: 
         form = CommentForm()

    return render(request, 'post_detail.html',  {'post':post, 'form':form})

 