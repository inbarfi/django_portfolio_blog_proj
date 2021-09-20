from django.db import models
from django.db.models.fields import EmailField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    #body = models.TextField() # remove
    date_added = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField("PostCategory", related_name='posts')   

    # by defalut it will order by id, changed to date_added:
    class Meta():
        ordering = ['-date_added']
    #method
    def cover_photo(self):
        return self.photos.filter(is_cover=True).first()

#instead of body
class PostParagraph(models.Model):
    subtitle = models.CharField(max_length=255)
    text = models.TextField()
    post = models.ForeignKey(Post, related_name='paragraphs', on_delete=models.CASCADE) 


class ParagraphPhoto(models.Model):
    image = models.ImageField()
    paragraph = models.ForeignKey(PostParagraph, related_name='photos', on_delete=models.CASCADE)   
    is_cover = models.BooleanField(default=False)


class ParagraphVideo(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    paragraph = models.ForeignKey(PostParagraph, related_name='videos', on_delete=models.CASCADE)   

    def __str__(self):
        return self.caption


class PostCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()


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