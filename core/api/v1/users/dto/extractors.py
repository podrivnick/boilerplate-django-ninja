from django.http import HttpRequest

from core.api.v1.users.dto.base import DTOAuthenticateAPI


def extract_authenticate_dto(
    request: HttpRequest,
) -> DTOAuthenticateAPI:
    is_authenticated = request.user.is_authenticated
    username = request.POST.get("username", "")
    email = request.POST.get("email", "")
    password = request.POST.get("password", "")
    session_key = request.session.session_key or False

    return DTOAuthenticateAPI(
        username=username,
        email=email,
        password=password,
        is_authenticated=is_authenticated,
        session_key=session_key,
    )
