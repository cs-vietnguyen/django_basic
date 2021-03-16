from django.db import models

from AccountContentManagement.domain.contants import UPVOTE, DOWNVOTE
from Common.domain.models import BaseModel
from Common.utils import pkgen


class UserAnswerVoteChoises(models.IntegerChoices):
    UPVOTE = UPVOTE, "UPVOTE"
    DOWNVOTE = DOWNVOTE, "DOWNVOTE"


class UserAnswerVote(BaseModel):
    id = models.UUIDField(max_length=40, primary_key=True, default=pkgen)
    account = models.ForeignKey(
        "AccountManagement.Account",
        on_delete=models.CASCADE,
        related_name="answer_votes",
    )
    answer = models.ForeignKey(
        "ContentManagement.Answer",
        on_delete=models.CASCADE,
        related_name="votes",
    )
    value = models.IntegerField(
        default=UserAnswerVoteChoises.UPVOTE, choices=UserAnswerVoteChoises.choices
    )

    class Meta:
        db_table = "user_answer_vote"
