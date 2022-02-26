from django.db import models
from django.utils.html import format_html
from django.utils.html import mark_safe


# Choices
STATUS = (
    ('Active', 'ACTIVE'),
    ('InActive', 'INACTIVE'),
)


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=300)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.TextField(default="")
    proContent = models.TextField(default="")
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def product_status(self):
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
    def product_image(self):
        return mark_safe('<img src="{}" width="160" height="130" />'.format(self.image.url))

    def __str__(self):
        return self.product_name



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUS, default='Active')
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def Status(self):
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

    def __str__(self):
            return str(self.order_id)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:80] + "..." + str(self.order_id)

