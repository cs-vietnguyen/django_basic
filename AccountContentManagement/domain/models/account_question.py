from django.db import models

from Common.domain.models import BaseModel
from Common.utils import pkgen


class AccountQuestion(BaseModel):
    id = models.UUIDField(max_length=40, primary_key=True, default=pkgen)
    account = models.ForeignKey(
        "AccountManagement.Account",
        on_delete=models.CASCADE,
        related_name="questions",
    )
    question = models.OneToOneField(
        "ContentManagement.Question",
        on_delete=models.CASCADE,
        related_name="account",
    )
    status = models.IntegerField(default=1)

    class Meta:
        db_table = "account_content"
