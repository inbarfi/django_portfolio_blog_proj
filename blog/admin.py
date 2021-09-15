from django.contrib import admin

# Register your models here.
from .models import Post, Comment, PostPhoto
#admin.site.register(Comment)

class PostPhotoInline(admin.StackedInline):
    model = PostPhoto
    extra = 0
    
class PostCommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    # list
    inlines = [PostPhotoInline, PostCommentInline]  
    list_display = ('title', 'date_added') 
    list_filter = ('date_added',)

admin.site.register(Post, PostAdmin)
