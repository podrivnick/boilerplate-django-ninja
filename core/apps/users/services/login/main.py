from dataclasses import dataclass

from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpRequest

from core.apps.users.entities.user import User as UserEntity
from core.apps.users.models import User
from core.apps.users.services.login.base import (
    BaseCommandAuthenticateUserService,
    BaseCommandVerificateUserService,
)


@dataclass
class ORMCommandVerificateUserService(BaseCommandVerificateUserService):
    def verificate_password(
        self,
        request: HttpRequest,
        user: UserEntity,
    ) -> User:
        return authenticate(
            request,
            username=user.username.to_raw(),
            password=user.password.to_raw(),
        )


@dataclass
class ORMCommandAuthenticateUserService(BaseCommandAuthenticateUserService):
    def login(
        self,
        user: User,
        request: HttpRequest,
    ) -> None:
        auth.login(request, user)
