from django.contrib import admin

# Register your models here.

from smwWeb.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Account, AccountAdmin)