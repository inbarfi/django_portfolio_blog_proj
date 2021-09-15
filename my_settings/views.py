from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .models import Project # ? FK - ProjectPhoto, ProjComment
from .forms import CommentForm

from .models import About, Home

# Create your views here.
# changed: posts = projects, post = project, all_posts = all_projects, blog = projects, post_detail = project_detail 

# def index(request):
#     projects = Project.objects.filter(is_featured = True)[0:2]
#     return render(request, 'home.html', {'projects':projects}) #context


def about(request):
    about_obj = About.objects.filter(is_active = True).last()
    return render(request, 'about.html', {'about': about_obj})


def home(request):
    home_obj = Home.objects.filter(is_active = True).last()
    projects = Project.objects.filter(is_featured = True)[0:2]
    # print(home_obj)
    return render(request, 'home.html', {'home': home_obj, 'projects':projects})


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

 

 