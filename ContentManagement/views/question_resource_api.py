from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ContentManagement.domain.models import Question
from ContentManagement.serializers import QuestionResourceSerializer


# class ContentListPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = "page_size"
#     max_page_size = 5000

class QuestionResourceAPI(ModelViewSet):
    authentication_classes = []
    permission_classes = []

    queryset = Question.objects.all()
    serializer_class = QuestionResourceSerializer
    # pagination_class = ContentListPagination

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filter_fields = ["tag"]
    search_fields = ["content", "tag"]
    ordering_fields = ["updated_at"]

    @swagger_auto_schema(
        operation_description="Get list question",
        operation_summary="Get list question",
        responses={204: {}},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
