from django.contrib import admin

admin.site.site_header = "My Website"


# Register your models here.
from .models import Project, ProjComment, ProjectPhoto, About, Home, Links, AboutPhoto
#admin.site.register(ProjComment)
#admin.site.register(About)
#admin.site.register(Links)

class AboutPhotoInline(admin.StackedInline):
    model = AboutPhoto
    extra = 0

class AboutAdmin(admin.ModelAdmin):
    # list
    inlines = [AboutPhotoInline] 
    list_display = ('title', 'is_active') 
    list_filter = ('title', 'is_active')

admin.site.register(About, AboutAdmin)




class ProjectPhotoInline(admin.StackedInline):
    model = ProjectPhoto
    extra = 0

class ProjCommentInline(admin.StackedInline):
    model = ProjComment
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    # list
    inlines = [ProjectPhotoInline, ProjCommentInline] 
    list_display = ('title', 'date_added', 'is_featured') 
    list_filter = ('date_added', 'is_featured')

admin.site.register(Project, ProjectAdmin)


 

class HomeLinksInline(admin.StackedInline):
    model = Links
    extra = 0


class HomeAdmin(admin.ModelAdmin):
    # list
    inlines = [HomeLinksInline]  
admin.site.register(Home, HomeAdmin)


 

# class PostAdmin(admin.ModelAdmin):
#     # list
#     inlines = [PostPhotoInline]  

# admin.site.register(Project, PostAdmin)