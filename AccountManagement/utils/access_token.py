import uuid
import time
from authlib.jose import jwt
from django.conf import settings

ACCESS_TOKEN_DUARATION = 86400 * 365


class AccessToken:
    def __init__(self, sub: str) -> None:
        self.sub = sub

    def generate(self):
        current_time = self.current_time()
        expire_time = self.expire_time(current_time)
        payload = {
            "iss": "Django-Basic",
            "sub": self.sub,
            "exp": expire_time,
            "iat": current_time,
            "jti": str(uuid.uuid4()),
        }
        return jwt.encode(
            settings.JWT_HEADER, payload, settings.JWT_PRIVATE_SIGNATURE
        ).decode("utf-8")

    def current_time(self):
        return int(time.time())

    def expire_time(self, timeline):
        return timeline + ACCESS_TOKEN_DUARATION
