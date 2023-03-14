from django.contrib import admin
from products.models import ProductCategory, Product, Basket

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
    list_display = ('id', 'name', 'category', 'price')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category')
    list_display_links = 'name',
    ordering = 'id',
    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
    extra = 0
    readonly_fields = ('created_timestamp',)
