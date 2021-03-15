from django.contrib import admin
from UserContentManagement.domain.models import AccountContent


@admin.register(AccountContent)
class AccountContentAdmin(admin.ModelAdmin):
    list_display = ("id", "account", "question", "status")
    empty_value_display = "-empty-"
