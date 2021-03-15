from django.template import context
from rest_framework import serializers
from drf_yasg.utils import swagger_serializer_method

from AccountManagement.domain.models import Account


class AccountSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "dob",
            "phone_number",
            "avatar",
            "access_token",
        ]

    @swagger_serializer_method(serializers.CharField)
    def get_access_token(self, account: Account):
        return self.context.get("access_token")
