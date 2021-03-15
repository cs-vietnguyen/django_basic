from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import ParseError

from Common.utils import Command, CommandHandler
from AccountManagement.serializers import AccountSerializer
from AccountManagement.domain.models import Account
from AccountManagement.utils import AccessToken


class SignInCommand(Command):
    username: str = ""
    password: str = ""

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password


class SignInCommandHandler(CommandHandler):
    def handle(self, command: SignInCommand):
        account = Account.objects.get(username=command.username)

        if not check_password(command.password, account.password):
            raise ParseError("Password is wrong")

        account.id = str(account.id)

        return AccountSerializer(
            account,
            context={"access_token": AccessToken(str(str(account.id))).generate()},
        ).data
