from django.contrib import messages
from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
    JsonResponse,
)
from django.urls import reverse

from core.api.schemas import (
    SuccessResponse,
    Template,
)
from core.api.v1.users.dto.responses import DTOResponseAuthenticateAPI


def render_authenticate(
    request: HttpRequest,
    response: SuccessResponse[DTOResponseAuthenticateAPI],
    template: Template,
) -> HttpResponse:
    """Возвращает либо JSON-ответ, либо HTML в зависимости от типа запроса."""
    if request.headers.get("Content-Type") == "application/json":
        return JsonResponse(
            {
                "status": response.status,
                "result": {
                    "username": response.result.username,
                },
            },
        )
    else:
        messages.success(request, f"{response.result.username} u've entered to profile")

        return HttpResponseRedirect(reverse("v1:index", args=["all"]))
