from rest_framework import serializers

from AccountContentManagement.app.dtos import CreateAnswerDto


class CreateAnswerRequestSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=200)

    def create(self, validated_data: dict):
        return CreateAnswerDto(**validated_data)
