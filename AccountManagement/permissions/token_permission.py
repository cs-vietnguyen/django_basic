from rest_framework.exceptions import APIException
from rest_framework import permissions


class TokenAuthenticatedShouldAwareRequestedUser(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        account_id = request.parser_context["kwargs"].get(
            "pk", request.parser_context["kwargs"].get("account_id", None)
        )

        if request.user == account_id:
            return request.user
        else:
            raise APIException(
                "Permission denied! You cannot access to the data you have just requested. Please login again to correct your account information"
            )
