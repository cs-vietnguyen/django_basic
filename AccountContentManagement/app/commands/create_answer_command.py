from Common.utils import Command, CommandHandler
from AccountContentManagement.app.dtos import CreateQuestionDto
from AccountContentManagement.domain.models import AccountQuestion
from ContentManagement.domain.models import Answer


class CreateAnswerCommand(Command):
    account_id: str
    question_id: str
    dto: CreateQuestionDto

    def __init__(
        self, account_id: str, question_id: str, dto: CreateQuestionDto
    ) -> None:
        self.account_id = account_id
        self.question_id = question_id
        self.dto = dto


class CreateAnswerCommandHandler(CommandHandler):
    def handle(self, command: CreateAnswerCommand):
        account_question = AccountQuestion.objects.get(
            account__id=command.account_id, question__id=command.question_id
        )
        Answer.objects.create(
            content=command.dto.content, question=account_question.question
        )
