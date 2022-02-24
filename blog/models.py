from django.db import models
from django.utils.html import format_html
from django.utils.html import mark_safe

STATUS = (
    ('Active', 'ACTIVE'),
    ('InActive', 'INACTIVE'),
)

# Create your models here.
class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images", default="")

    def blog_status(self):
        # print(self.status)
        if(self.status == "Active"):
            return format_html(
                '<span style="color: {};">{}</span>',
                "green",
                "Active",
                )
        else:
            return format_html(
                '<span style="color: {};">{}</span>',
                "red",
                "InActive",
                )

    @property            
    def blog_image(self):
        return mark_safe('<img src="{}" width="160" height="130" />'.format(self.thumbnail.url))

    def __str__(self):
        return self.title