from rest_framework import serializers

from ContentManagement.domain.models import Answer


class AnswerResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["id", "content"]
