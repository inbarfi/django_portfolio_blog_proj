from django.contrib import admin

# Register your models here.
from .models import Project, ProjComment, ProjectPhoto
admin.site.register(ProjComment)

class ProjectPhotoInline(admin.StackedInline):
    model = ProjectPhoto
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    # list
    inlines = [ProjectPhotoInline]  

admin.site.register(Project, ProjectAdmin)

 

# class PostAdmin(admin.ModelAdmin):
#     # list
#     inlines = [PostPhotoInline]  

# admin.site.register(Project, PostAdmin)