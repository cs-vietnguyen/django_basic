from rest_framework import serializers

from AccountContentManagement.serializers import UserAnswerResourceSerializer


class UserAnswerResponseSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=50)
    answers = UserAnswerResourceSerializer(many=True)

    class Meta:
        fields = [
            "question",
            "answers",
        ]
