from drf_yasg import openapi
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from AccountManagement.authentication import TokenAuthentication
from AccountManagement.permissions import TokenAuthenticatedShouldAwareRequestedUser
from AccountContentManagement.serializers.requests import (
    UserAnswerVoteRequestSerializer,
)
from AccountContentManagement.app.dtos import UserAnswerVoteDto
from AccountContentManagement.app.commands import UserAnswerVoteCommand
from Common.views import reponses
from Common.utils import Bus


class UserAnswerVoteAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TokenAuthenticatedShouldAwareRequestedUser]
    __bus: Bus = Bus()

    @swagger_auto_schema(
        operation_description="Create voting to answer of question",
        operation_summary="Create voting to answer of question",
        manual_parameters=[
            openapi.Parameter(
                "Authorization",
                openapi.IN_HEADER,
                description="Access token",
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ],
        request_body=UserAnswerVoteRequestSerializer,
        responses={200: "Success"},
    )
    def post(self, request, *arg, **karg):
        request_data = UserAnswerVoteRequestSerializer(data=request.data)
        request_data.is_valid()
        account_id = request.user
        question_id = karg.get("question_id")
        answer_id = karg.get("answer_id")
        dto: UserAnswerVoteDto = request_data.save()

        self.__bus.dispatch(
            UserAnswerVoteCommand(account_id, question_id, answer_id, dto)
        )

        return reponses.success({"mesage": "Success"})
