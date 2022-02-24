from django.contrib import admin

# Register your models here.
from .models import Blogpost

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ("post_id", "title", "blog_status", "pub_date", "blog_image")
admin.site.register(Blogpost, BlogpostAdmin)\
