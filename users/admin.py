from django.contrib import admin
from users.models import User
from products.admin import BasketAdmin

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'id', 'username', 'first_name', 'last_name', 'email'
    list_display_links = 'username',
    inlines = (BasketAdmin,)
    ordering = 'id',

