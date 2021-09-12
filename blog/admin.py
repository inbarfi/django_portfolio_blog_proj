from django.contrib import admin

# Register your models here.
from .models import Post, Comment, PostPhoto
admin.site.register(Comment)

class PostPhotoInline(admin.StackedInline):
    model = PostPhoto
    extra = 0
    
class PostAdmin(admin.ModelAdmin):
    # list
    inlines = [PostPhotoInline]  

admin.site.register(Post, PostAdmin)
