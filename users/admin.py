from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerification, User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'id', 'username', 'first_name', 'last_name', 'email'
    list_display_links = 'username',
    inlines = (BasketAdmin,)
    ordering = 'id',


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
