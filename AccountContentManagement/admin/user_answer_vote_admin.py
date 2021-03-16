from django.contrib import admin
from AccountContentManagement.domain.models import UserAnswerVote


@admin.register(UserAnswerVote)
class UserAnswerVoteAdmin(admin.ModelAdmin):
    list_display = ("id", "account", "answer", "value")
    empty_value_display = "-empty-"
