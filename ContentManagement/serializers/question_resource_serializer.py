from rest_framework import serializers

from ContentManagement.domain.models import Question
from AccountManagement.serializers import AccountSerializer


class QuestionResourceSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField(source="get_creator")
    class Meta:
        model = Question
        fields = ["id", "creator", "content", "type", "tag"]

    def get_creator(self, question: Question):
        return AccountSerializer(question.account.account).data