from Common.utils import Command, CommandHandler
from AccountManagement.domain.models import Account
from AccountContentManagement.app.dtos import UserAnswerVoteDto
from AccountContentManagement.domain.models import UserAnswerVote
from ContentManagement.domain.models import Answer


class UserAnswerVoteCommand(Command):
    account_id: str
    question_id: str
    answer_id: str
    dto: UserAnswerVoteDto

    def __init__(
        self, account_id: str, question_id: str, answer_id: str, dto: UserAnswerVoteDto
    ) -> None:
        self.account_id = account_id
        self.question_id = question_id
        self.answer_id = answer_id
        self.dto = dto


class UserAnswerVoteCommandHandler(CommandHandler):
    def handle(self, command: UserAnswerVoteCommand):
        account = Account.objects.get(id=command.account_id)
        answer = Answer.objects.get(
            id=command.answer_id, question__id=command.question_id
        )
        UserAnswerVote.objects.create(
            account=account, answer=answer, value=command.dto.value
        )
