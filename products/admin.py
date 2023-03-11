from django.contrib import admin
from products.models import ProductCategory, Product

# Register your models here.
# admin.site.register(Product)
admin.site.register(ProductCategory)


# @admin.register(ProductCategory)
# class ProductCategoryAdmin(admin.ModelAdmin):
#     list_display = 'id', 'name'
#     list_display_links = 'name',
#     ordering = 'id',

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'category', 'price'
    list_display_links = 'name',
    ordering = 'id',