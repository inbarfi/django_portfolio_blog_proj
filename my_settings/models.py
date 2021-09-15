from django.db import models
from django.db.models.fields import EmailField, URLField
from django.db.models.fields.related import ForeignKey

# Create your models here.
# changed: Post = Project, PostPhoto = ProjectPhoto, post = project
class Project(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    # by defalut it will order by id, changed to date_added:
    class Meta():
        ordering = ['-date_added']
    #method
    def cover_photo(self):
        return self.photos.filter(is_cover=True).first()
    

class ProjectPhoto(models.Model):
    image = models.ImageField()
    project = models.ForeignKey(Project, related_name='photos', on_delete=models.CASCADE)   
    is_cover = models.BooleanField(default=False)


class ProjComment(models.Model):
    project = models.ForeignKey(Project, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta():
        ordering = ['date_added']

class ProjectVideo(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")
    project = models.ForeignKey(Project, related_name='videos', on_delete=models.CASCADE)   #?

    def __str__(self):
        return self.caption


class About(models.Model):
    title = models.CharField(max_length=255, default="About")
    content = models.TextField()
    is_active = models.BooleanField(default=False)

    #method
    def background_image(self):
        return self.photos.filter(is_background=True).first()

    class Meta():
        verbose_name_plural = 'About'

class AboutPhoto(models.Model):
    image = models.ImageField()
    about = models.ForeignKey(About, related_name='photos', on_delete=models.CASCADE)   
    is_background = models.BooleanField(default=False)


class Home(models.Model):
    title = models.CharField(max_length=255, default="Welcome!")
    intro = models.CharField(max_length=500)
    background_image = models.ImageField()
    is_active = models.BooleanField(default=False)

    class Meta():
        verbose_name_plural = 'Home'

class Links(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=50)
    home = models.ForeignKey(Home, related_name='links', on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Link'
    

