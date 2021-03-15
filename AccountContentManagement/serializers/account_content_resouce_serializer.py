from rest_framework import serializers

from AccountContentManagement.domain.models import AccountQuestion
from ContentManagement.serializers import QuestionResourceSerializer


class AccountQuestionResourceSerializer(serializers.ModelSerializer):
    question = QuestionResourceSerializer()

    class Meta:
        model = AccountQuestion
        fields = ["id", "question"]
