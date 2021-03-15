from django.db import models

from Common.domain.models import BaseModel
from Common.utils import pkgen


class Answer(BaseModel):
    id = models.UUIDField(max_length=40, primary_key=True, default=pkgen)
    content = models.CharField(max_length=200)
    status = models.IntegerField(default=1)
    question = models.ForeignKey(
        "Question",
        on_delete=models.CASCADE,
        related_name="answers",
    )

    class Meta:
        db_table = "answer"
