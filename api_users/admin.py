from django.contrib import admin

from api_users.models import CustomUser


class AdminAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'confirmation_code',
        'pk'
    )
    search_fields = ('email',)
    list_filter = ('email',)
    empty_value_display = '-пусто-'


try:
    admin.site.register(CustomUser, AdminAdmin)
except admin.sites.AlreadyRegistered:
    pass
