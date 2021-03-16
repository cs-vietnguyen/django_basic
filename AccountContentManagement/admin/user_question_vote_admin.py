from django.contrib import admin
from AccountContentManagement.domain.models import UserQuestionVote


@admin.register(UserQuestionVote)
class UserQuestionVoteAdmin(admin.ModelAdmin):
    list_display = ("id", "account", "question", "value")
    empty_value_display = "-empty-"
