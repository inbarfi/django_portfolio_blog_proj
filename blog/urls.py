from django.urls import path
from . import views


urlpatterns = [
    #blog/nothing:
    path('about/', views.about, name='about'),
    path('', views.all_posts, name='all_posts'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
]



