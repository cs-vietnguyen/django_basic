from django.conf.urls import url, include
from ContentManagement.views import QuestionResourceAPI

urlpatterns = [
    url(r"", QuestionResourceAPI.as_view({"get": "list"})),
]
