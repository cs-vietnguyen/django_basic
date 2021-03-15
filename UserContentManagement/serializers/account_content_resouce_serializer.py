from rest_framework import serializers

from UserContentManagement.domain.models import AccountContent
from ContentManagement.serializers import QuestionResourceSerializer


class AccountContentResourceSerializer(serializers.ModelSerializer):
    question = QuestionResourceSerializer()

    class Meta:
        model = AccountContent
        fields = ["id", "question"]
