from django.db import models
from django.db.models.fields import EmailField
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