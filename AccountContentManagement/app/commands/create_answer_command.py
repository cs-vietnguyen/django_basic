from Common.utils import Command, CommandHandler
from AccountManagement.domain.models import Account
from AccountContentManagement.app.dtos import CreateQuestionDto
from AccountContentManagement.domain.models import UserAnswer
from ContentManagement.domain.models import Question, Answer


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
        account = Account.objects.get(id=command.account_id)
        question = Question.objects.get(id=command.question_id)
        answer = Answer.objects.create(content=command.dto.content, question=question)
        UserAnswer.objects.create(account=account, answer=answer)
