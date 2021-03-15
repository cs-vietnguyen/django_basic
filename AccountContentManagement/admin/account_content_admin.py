from django.contrib import admin
from AccountContentManagement.domain.models import AccountQuestion


@admin.register(AccountQuestion)
class AccountQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "account", "question", "status")
    empty_value_display = "-empty-"
