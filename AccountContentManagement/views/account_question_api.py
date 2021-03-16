from AccountContentManagement.domain.models import AccountQuestion
from drf_yasg import openapi
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from AccountManagement.authentication import TokenAuthentication
from AccountManagement.permissions import TokenAuthenticatedShouldAwareRequestedUser
from AccountContentManagement.serializers import (
    AccountQuestionSerializer,
    AccountQuestionResourceSerializer,
)
from AccountContentManagement.serializers.requests import (
    CreateQuestionRequestSerializer,
)
from AccountContentManagement.app.dtos import CreateQuestionDto
from AccountContentManagement.app.commands import CreateAccountQuestionCommand
from Common.views import reponses
from Common.utils import Bus


class AccountQuestionAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [TokenAuthenticatedShouldAwareRequestedUser]
    __bus: Bus = Bus()

    @swagger_auto_schema(
        operation_description="Create question",
        operation_summary="Create question",
        manual_parameters=[
            openapi.Parameter(
                "Authorization",
                openapi.IN_HEADER,
                description="Access token",
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ],
        request_body=CreateQuestionRequestSerializer,
        responses={200: "Success"},
    )
    def post(self, request, *arg, **karg):
        request_data = CreateQuestionRequestSerializer(data=request.data)
        request_data.is_valid()
        account_id = request.user
        dto: CreateQuestionDto = request_data.save()

        self.__bus.dispatch(CreateAccountQuestionCommand(account_id, dto))

        return reponses.success({"mesage": "Success"})

    @swagger_auto_schema(
        operation_description="Get list question of account",
        operation_summary="Get list question of account",
        manual_parameters=[
            openapi.Parameter(
                "Authorization",
                openapi.IN_HEADER,
                description="Access token",
                required=True,
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={200: AccountQuestionSerializer},
    )
    def get(self, request, *arg, **karg):
        request_data = CreateQuestionRequestSerializer(data=request.data)
        request_data.is_valid()

        questions = AccountQuestionResourceSerializer(
            AccountQuestion.objects.filter(account__id=request.user), many=True
        ).data
        data_response = {"data": {"account": request.user, "questions": questions}}

        return reponses.success(data_response)
