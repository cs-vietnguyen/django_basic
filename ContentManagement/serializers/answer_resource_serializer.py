from rest_framework import serializers

from ContentManagement.domain.models import Answer
from AccountManagement.serializers import AccountSerializer
from AccountContentManagement.serializers.user_answer_vote_resource_serializer import UserAnswerVoteResourceSerializer


class AnswerResourceSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField(source="get_creator")
    votes = serializers.SerializerMethodField(source="get_votes")
    class Meta:
        model = Answer
        fields = ["id", "creator", "content", "votes"]

    def get_creator(self, answer: Answer):
        return AccountSerializer(answer.account.account).data
    
    def get_votes(self, answer: Answer):
        return UserAnswerVoteResourceSerializer(answer.votes.all(), many=True).data