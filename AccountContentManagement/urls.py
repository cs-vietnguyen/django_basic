from django.conf.urls import url, include
from AccountContentManagement.views import (
    AccountQuestionAPI,
    UserAnswerAPI,
    UserQuestionVoteAPI,
    UserAnswerVoteAPI,
)

urlpatterns = [
    url(r"(?P<account_id>[\w-]+)/questions/$", AccountQuestionAPI.as_view()),
    url(
        r"(?P<account_id>[\w-]+)/questions/(?P<question_id>[\w-]+)/answers$",
        UserAnswerAPI.as_view(),
    ),
    url(
        r"(?P<account_id>[\w-]+)/questions/(?P<question_id>[\w-]+)/votes$",
        UserQuestionVoteAPI.as_view(),
    ),
    url(
        r"(?P<account_id>[\w-]+)/questions/(?P<question_id>[\w-]+)/answers/(?P<answer_id>[\w-]+)/votes$",
        UserAnswerVoteAPI.as_view(),
    ),
]
