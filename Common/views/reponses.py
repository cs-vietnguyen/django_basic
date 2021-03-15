from django.http import JsonResponse
from rest_framework import status


def success(data):
    # localize message here
    # custom data here
    return JsonResponse(
        data,
        safe=False,
        status=status.HTTP_200_OK,
    )
