from django.contrib import admin
from ContentManagement.domain.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "status", "type")
    empty_value_display = "-empty-"
