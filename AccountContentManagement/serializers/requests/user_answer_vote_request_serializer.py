from rest_framework import serializers

from AccountContentManagement.app.dtos import UserAnswerVoteDto
from AccountContentManagement.domain.models.user_answer_vote import (
    UserAnswerVoteChoises,
)


class UserAnswerVoteRequestSerializer(serializers.Serializer):
    value = serializers.ChoiceField(
        default=UserAnswerVoteChoises.UPVOTE, choices=UserAnswerVoteChoises.choices
    )

    def create(self, validated_data: dict):
        return UserAnswerVoteDto(**validated_data)
