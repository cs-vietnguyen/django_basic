from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from Common.views import reponses
from Common.utils import Bus
from AccountManagement.app.commands import SignUpCommand
from AccountManagement.serializers.requests import SignUpRequestSerializer


class SignUpAPI(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        operation_description="Sign in to system via API",
        operation_summary="Sign in to system via API",
        request_body=SignUpRequestSerializer,
        responses={200: "Success"},
    )
    def post(self, request, format=None):
        request_data = SignUpRequestSerializer(data=request.data)
        request_data.is_valid(raise_exception=True)
        sign_up_dto = request_data.save()

        __bus: Bus = Bus()

        __bus.dispatch(SignUpCommand(sign_up_dto))

        return reponses.success("Thành công nha")
