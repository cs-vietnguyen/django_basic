from django.db import models

from AccountContentManagement.domain.contants import UPVOTE, DOWNVOTE
from Common.domain.models import BaseModel
from Common.utils import pkgen


class UserQuestionVoteChoises(models.IntegerChoices):
    UPVOTE = UPVOTE, "UPVOTE"
    DOWNVOTE = DOWNVOTE, "DOWNVOTE"


class UserQuestionVote(BaseModel):
    id = models.UUIDField(max_length=40, primary_key=True, default=pkgen)
    account = models.ForeignKey(
        "AccountManagement.Account",
        on_delete=models.CASCADE,
        related_name="question_votes",
    )
    question = models.ForeignKey(
        "ContentManagement.Question",
        on_delete=models.CASCADE,
        related_name="votes",
    )
    value = models.IntegerField(
        default=UserQuestionVoteChoises.UPVOTE, choices=UserQuestionVoteChoises.choices
    )

    class Meta:
        db_table = "user_question_vote"
