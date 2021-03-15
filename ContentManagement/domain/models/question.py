from django.db import models

from Common.domain.models import BaseModel
from Common.utils import pkgen
from ContentManagement.domain.contants import MULTICHOICE, SELECT, TYPING


class QuestionTypeChoises(models.IntegerChoices):
    MULTICHOICE = MULTICHOICE, "Multichoice"
    SELECT = SELECT, "Selec"
    TYPING = TYPING, "Typing"


class Question(BaseModel):
    id = models.UUIDField(max_length=40, primary_key=True, default=pkgen)
    content = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    type = models.IntegerField(
        default=QuestionTypeChoises.SELECT, choices=QuestionTypeChoises.choices
    )

    class Meta:
        db_table = "question"

    def __str__(self) -> str:
        return self.content
