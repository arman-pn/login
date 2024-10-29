from django.contrib import admin
from .models import UserAccounts
class UserAccountsAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccounts , UserAccountsAdmin)
