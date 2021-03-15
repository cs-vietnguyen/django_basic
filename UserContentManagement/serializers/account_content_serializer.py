from rest_framework import serializers

from UserContentManagement.serializers import AccountContentResourceSerializer


class AccountContentSerializer(serializers.Serializer):
    account = serializers.CharField(max_length=50)
    questions = AccountContentResourceSerializer(many=True)

    class Meta:
        fields = [
            "account",
            "question",
        ]
