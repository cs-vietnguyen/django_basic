from django.conf.urls import url, include
from AccountContentManagement.views import (
    CreateQuestionAPI,
    CreateAnswerAPI,
    UserQuestionVoteAPI,
    UserAnswerVoteAPI,
)

urlpatterns = [
    url(r"(?P<account_id>[\w-]+)/questions/$", CreateQuestionAPI.as_view()),
    url(
        r"(?P<account_id>[\w-]+)/questions/(?P<question_id>[\w-]+)/answers$",
        CreateAnswerAPI.as_view(),
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
