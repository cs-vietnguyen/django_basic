from rest_framework import serializers

from AccountContentManagement.app.dtos import UserQuestionVoteDto
from AccountContentManagement.domain.models.user_question_vote import (
    UserQuestionVoteChoises,
)


class UserQuestionVoteRequestSerializer(serializers.Serializer):
    value = serializers.ChoiceField(
        default=UserQuestionVoteChoises.UPVOTE, choices=UserQuestionVoteChoises.choices
    )

    def create(self, validated_data: dict):
        return UserQuestionVoteDto(**validated_data)
