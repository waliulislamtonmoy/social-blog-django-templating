from django.contrib import admin

# Register your models here.

from .models import Blog,Comment

class BlogAdmin(admin.ModelAdmin):
    list_display=["id",'author','title','category','image',"date",'update']
    ordering=['id']
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment )