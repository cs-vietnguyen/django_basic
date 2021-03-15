from rest_framework import serializers

from AccountContentManagement.serializers import AccountQuestionResourceSerializer


class AccountQuestionSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=50)
    questions = AccountQuestionResourceSerializer(many=True)

    class Meta:
        fields = [
            "account",
            "question",
        ]
