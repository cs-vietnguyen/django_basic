from django.contrib import admin
from ContentManagement.domain.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "question", "status")
    empty_value_display = "-empty-"
