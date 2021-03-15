from authlib.jose import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise NotAuthenticated(_("Token not found!"))

        try:
            json_profile = jwt.decode(token, settings.JWT_PRIVATE_SIGNATURE)
            sub: str = json_profile["sub"]
        except Exception as ex:
            raise AuthenticationFailed(
                "Please log in again to update your account information."
            )

        return (sub, json_profile)
