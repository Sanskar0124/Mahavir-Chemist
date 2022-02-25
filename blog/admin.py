from django.contrib import admin

# Register your models here.
from .models import Blogpost

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ("post_id", "title", "blog_status", "pub_date", "blog_image")
    class Media:
        js = ('tinyInjectBlogpost.js',)
# admin.site.register(BlogpostAdmin)
