from django.contrib import admin
from AccountContentManagement.domain.models import UserAnswer


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "account", "answer", "status")
    empty_value_display = "-empty-"
