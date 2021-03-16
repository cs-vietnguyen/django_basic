from Common.utils import Command, CommandHandler
from AccountManagement.domain.models import Account
from AccountContentManagement.app.dtos import UserQuestionVoteDto
from AccountContentManagement.domain.models import UserQuestionVote
from ContentManagement.domain.models import Question


class UserQuestionVoteCommand(Command):
    account_id: str
    question_id: str
    dto: UserQuestionVoteDto

    def __init__(
        self, account_id: str, question_id: str, dto: UserQuestionVoteDto
    ) -> None:
        self.account_id = account_id
        self.question_id = question_id
        self.dto = dto


class UserQuestionVoteCommandHandler(CommandHandler):
    def handle(self, command: UserQuestionVoteCommand):
        account = Account.objects.get(id=command.account_id)
        question = Question.objects.get(id=command.question_id)
        UserQuestionVote.objects.create(
            account=account, question=question, value=command.dto.value
        )
