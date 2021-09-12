from django.urls import path
from . import views


urlpatterns = [
    #blog/nothing:
    path('', views.index, name='index'),
    
    path('about/', views.about, name='about'),
    path('blog/', views.all_posts, name='all_posts'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]



