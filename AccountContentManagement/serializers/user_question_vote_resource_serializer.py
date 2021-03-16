from rest_framework import serializers

from AccountContentManagement.domain.models import UserQuestionVote


class UserQuestionVoteResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuestionVote
        fields = ["id", "value"]
