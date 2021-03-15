from rest_framework import serializers

from ContentManagement.domain.models import Question


class QuestionResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "content", "type"]
