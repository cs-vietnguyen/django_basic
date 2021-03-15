from Common.utils import Command, CommandHandler
from AccountManagement.domain.models import Account
from AccountManagement.serializers.dtos import SignUpRequestDto


class SignUpCommand(Command):
    dto: SignUpRequestDto = None

    def __init__(self, dto: SignUpRequestDto) -> None:
        self.dto = dto


class SignUpCommandHandler(CommandHandler):
    def handle(self, command: SignUpCommand):
        Account.objects.create(**(command.dto.__dict__))
