from rest_framework import serializers

from AccountContentManagement.domain.models import UserAnswerVote


class UserAnswerVoteResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswerVote
        fields = ["id", "value"]
