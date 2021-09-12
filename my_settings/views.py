from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .models import Project
from .forms import CommentForm

# Create your views here.
# changed: posts = projects, post = project, all_posts = all_projects, blog = projects, post_detail = project_detail 

def index(request):
    projects = Project.objects.filter(is_featured = True)[0:2]
    return render(request, 'home.html', {'projects':projects}) #context


def about(request):
    return render(request, 'about.html')

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects':projects})
#.all

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()

            return redirect('project_detail', slug=project.slug)
    else: 
         form = CommentForm()

    return render(request, 'project_detail.html',  {'project':project, 'form':form})

 

 