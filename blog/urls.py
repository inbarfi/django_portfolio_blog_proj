from django.urls import path
from . import views


urlpatterns = [
    #blog/nothing:
    path('', views.all_posts, name='all_posts'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.post_by_category, name='post_by_category'),
]



