from django.http import (
    HttpRequest,
    HttpResponse,
)
from ninja import Router

from core.api.schemas import SuccessResponse
from core.api.v1.users.dto.extractors import extract_authenticate_dto
from core.api.v1.users.dto.responses import DTOResponseAuthenticateAPI
from core.api.v1.users.renders import render_authenticate
from core.apps.users.use_cases.login import AuthenticatePageCommand
from core.infrastructure.di.main import init_container
from core.infrastructure.exceptions.base import BaseAppException
from core.infrastructure.mediator.mediator import Mediator


router = Router(tags=["user"])


@router.post(
    "login_post",
    url_name="login_post",
)
def login_post(
    request: HttpRequest,
) -> HttpResponse:
    """API: Аутентификации и Авторизации."""
    container = init_container()
    mediator: Mediator = container.resolve(Mediator)

    authenticate_request_dto = extract_authenticate_dto(
        request=request,
    )

    try:
        dto_response_authenticate_api: DTOResponseAuthenticateAPI = (
            mediator.handle_command(
                AuthenticatePageCommand(
                    username=authenticate_request_dto.username,
                    email=authenticate_request_dto.email,
                    password=authenticate_request_dto.password,
                    session_key=authenticate_request_dto.session_key,
                    is_authenticated=authenticate_request_dto.is_authenticated,
                    request=request,
                ),
            )[0]
        )
    except BaseAppException as exception:
        raise ValueError(
            detail={"error": exception.exception},
        )

    return render_authenticate(
        request=request,
        response=SuccessResponse(result=dto_response_authenticate_api),
        template="main_favorite/index.html",
    )
