from functools import lru_cache

from punq import Container

from core.apps.users.services.login.main import (
    ORMCommandAuthenticateUserService,
    ORMCommandVerificateUserService,
)
from core.apps.users.use_cases.login import (
    AuthenticatePageCommand,
    AuthenticatePageCommandHandler,
)
from core.infrastructure.mediator.mediator import Mediator


@lru_cache(1)
def init_container() -> Container:
    return _initialize_container()


def _initialize_container() -> Container:
    container = Container()

    # init services

    # Handlers
    container.register(AuthenticatePageCommandHandler)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        # command handlers
        # user app
        configure_authentice_handler = AuthenticatePageCommandHandler(
            command_verificate_password_service=ORMCommandVerificateUserService(),
            command_authenticate_user_service=ORMCommandAuthenticateUserService(),
        )

        # commands
        # user app
        mediator.register_command(
            AuthenticatePageCommand,
            [configure_authentice_handler],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
