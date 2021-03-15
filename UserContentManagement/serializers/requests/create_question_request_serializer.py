from rest_framework import serializers

from UserContentManagement.app.dtos import CreateQuestionDto


class CreateQuestionRequestSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=200)
    type = serializers.IntegerField(default=1)

    def create(self, validated_data: dict):
        return CreateQuestionDto(**validated_data)
