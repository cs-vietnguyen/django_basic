from django.conf.urls import url, include
from AccountContentManagement.views import CreateQuestionAPI, CreateAnswerAPI

urlpatterns = [
    url(r"(?P<account_id>[\w-]+)/questions/$", CreateQuestionAPI.as_view()),
    url(
        r"(?P<account_id>[\w-]+)/questions/(?P<question_id>[\w-]+)/answers$",
        CreateAnswerAPI.as_view(),
    ),
]
