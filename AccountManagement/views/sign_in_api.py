from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from AccountManagement.serializers import AccountSerializer
from AccountManagement.serializers.requests import SignInRequestSerializer
from AccountManagement.app.commands import SignInCommand
from Common.views import reponses
from Common.utils import Bus


class SignInAPI(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Sign in to system via API",
        operation_summary="Sign in to system via API",
        request_body=SignInRequestSerializer,
        responses={200: AccountSerializer},
    )
    def post(self, request, format=None):
        request_data = SignInRequestSerializer(data=request.data)
        request_data.is_valid()

        __bus: Bus = Bus()

        data_response = __bus.dispatch(SignInCommand(**request_data.data))

        return reponses.success(data_response)
