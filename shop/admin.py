from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInjectShop.js',)
    list_display = ("product_name", "category", "pub_date", "price", "product_status", "product_image")
# admin.site.register(Product, ProductAdmin)

class OrderUpdateAdmin(admin.ModelAdmin):
    list_display = ("order_id", "update_desc", "timestamp")
admin.site.register(OrderUpdate, OrderUpdateAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ("order_id", "email", "amount", "Status", "name", "city", "phone", "zip_code")
admin.site.register(Orders, OrdersAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("msg_id", "name", "email", "phone")
admin.site.register(Contact, ContactAdmin)