from rest_framework import serializers

from AccountManagement.serializers import AccountSerializer
from AccountContentManagement.domain.models import UserAnswer
from ContentManagement.serializers import AnswerResourceSerializer


class UserAnswerResourceSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    answer = AnswerResourceSerializer()

    class Meta:
        model = UserAnswer
        fields = ["id", "account", "answer"]
