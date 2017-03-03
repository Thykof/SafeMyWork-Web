from django.contrib import admin

# Register your models here.

from smwWeb.models import Account, SettingsFile

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user',)

class SettingsFileAdmin(admin.ModelAdmin):
	list_display = ('settings_file', 'account')

admin.site.register(Account, AccountAdmin)
admin.site.register(SettingsFile, SettingsFileAdmin)