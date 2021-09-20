from django.contrib import admin

# Register your models here.
from .models import Post, Comment, PostPhoto, PostCategory, PostParagraph, ParagraphVideo, ParagraphPhoto
#admin.site.register(Comment)
admin.site.register(PostCategory)

class PostPhotoInline(admin.StackedInline):
    model = PostPhoto
    extra = 0
    
class PostCommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostParagraphInline(admin.StackedInline):
    model = PostParagraph
    extra = 0

class ParagraphPhotoInline(admin.StackedInline):
    model = ParagraphPhoto
    extra = 0

class ParagraphVideoInline(admin.StackedInline):
    model = ParagraphVideo
    extra = 0

class PostAdmin(admin.ModelAdmin):
    # list
    inlines = [PostPhotoInline, PostCommentInline]  
    list_display = ('title', 'date_added') 
    list_filter = ('date_added',)

admin.site.register(Post, PostAdmin)


class PostParagraphAdmin(admin.ModelAdmin):
    # list
    inlines = [ParagraphPhotoInline, ParagraphVideoInline]  

admin.site.register(PostParagraph, PostParagraphAdmin)