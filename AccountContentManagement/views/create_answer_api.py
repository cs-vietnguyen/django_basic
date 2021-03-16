from drf_yasg import openapi
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from AccountManagement.authentication import TokenAuthentication
from AccountManagement.permissions import TokenAuthenticatedShouldAwareRequestedUser
from ContentManagement.domain.models import Answer
from AccountContentManagement.domain.models import UserAnswer
from AccountContentManagement.serializers import UserAnswerResourceSerializer
from AccountContentManagement.serializers.requests import CreateAnswerRequestSerializer
from AccountContentManagement.serializers.responses import UserAnswerResponseSerializer
from AccountContentManagement.app.dtos import CreateAnswerDto
from AccountContentManagement.app.commands import CreateAnswerCommand
from Common.views import reponses
from Common.utils import Bus


class CreateAnswerAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TokenAuthenticatedShouldAwareRequestedUser]
    __bus: Bus = Bus()

    @swagger_auto_schema(
        operation_description="Create answer to question",
        operation_summary="Create answer to question",
        manual_parameters=[
            openapi.Parameter(
                "Authorization",
                openapi.IN_HEADER,
                description="Access token",
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ],
        request_body=CreateAnswerRequestSerializer,
        responses={200: "Success"},
    )
    def post(self, request, *arg, **karg):
        request_data = CreateAnswerRequestSerializer(data=request.data)
        request_data.is_valid()
        account_id = request.user
        question_id = karg.get("question_id")
        dto: CreateAnswerDto = request_data.save()

        self.__bus.dispatch(CreateAnswerCommand(account_id, question_id, dto))

        return reponses.success({"mesage": "Success"})

    @swagger_auto_schema(
        operation_description="Get list answer of question",
        operation_summary="Get list answer of question",
        manual_parameters=[
            openapi.Parameter(
                "Authorization",
                openapi.IN_HEADER,
                description="Access token",
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: UserAnswerResponseSerializer},
    )
    def get(self, request, *arg, **karg):
        question_id = karg.get("question_id")
        answers = Answer.objects.filter(question__id=question_id).values_list("id")

        user_answer = UserAnswerResourceSerializer(
            UserAnswer.objects.filter(answer__id__in=answers), many=True
        ).data
        data_response = {"data": {"question": question_id, "answers": user_answer}}

        return reponses.success(data_response)
