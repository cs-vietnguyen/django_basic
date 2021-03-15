from Common.utils import Command, CommandHandler
from AccountManagement.domain.models import Account
from AccountContentManagement.app.dtos import CreateQuestionDto
from AccountContentManagement.domain.models import AccountQuestion
from ContentManagement.domain.models import Question


class CreateAccountQuestionCommand(Command):
    account_id: str
    dto: CreateQuestionDto

    def __init__(self, account_id: str, dto: CreateQuestionDto) -> None:
        self.account_id = account_id
        self.dto = dto


class CreateAccountQuestionCommandHandler(CommandHandler):
    def handle(self, command: CreateAccountQuestionCommand):
        account = Account.objects.get(id=command.account_id)
        question = Question.objects.create(
            content=command.dto.content, type=command.dto.type
        )
        AccountQuestion.objects.create(account=account, question=question)
