from rest_framework import serializers

from ContentManagement.domain.models import Question
from ContentManagement.serializers.answer_resource_serializer import AnswerResourceSerializer
from AccountManagement.serializers import AccountSerializer
from AccountContentManagement.serializers.user_question_vote_resource_serializer import UserQuestionVoteResourceSerializer


class QuestionResourceSerializer(serializers.ModelSerializer):
    creator = serializers.SerializerMethodField(source="get_creator")
    answers = serializers.SerializerMethodField(source="get_answers")
    votes = serializers.SerializerMethodField(source="get_votes")
    class Meta:
        model = Question
        fields = ["id", "creator", "answers", "votes", "content", "type", "tag"]

    def get_creator(self, question: Question):
        return AccountSerializer(question.account.account).data

    def get_answers(self, question: Question):
        return AnswerResourceSerializer(question.answers.all(), many=True).data

    def get_votes(self, question: Question):
            return UserQuestionVoteResourceSerializer(question.votes.all(), many=True).data