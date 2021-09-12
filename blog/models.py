from django.db import models
from django.db.models.fields import EmailField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField() # change to char
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # by defalut it will order by id, changed to date_added:
    class Meta():
        ordering = ['-date_added']
    #method
    def cover_photo(self):
        return self.photos.filter(is_cover=True).first()



class PostPhoto(models.Model):
    image = models.ImageField()
    post = models.ForeignKey(Post, related_name='photos', on_delete=models.CASCADE)   
    is_cover = models.BooleanField(default=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        ordering = ['date_added']