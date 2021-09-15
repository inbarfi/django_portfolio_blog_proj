from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #path('blog/', views.all_posts, name='all_posts'),
    path('projects/', views.all_projects, name='all_projects'),
    #path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
]
