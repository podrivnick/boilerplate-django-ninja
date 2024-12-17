from functools import lru_cache

from punq import Container

from core.apps.users.use_cases.login import (
    LoginPageCommand,
    LoginPageCommandHandler,
)
from core.infrastructure.mediator.mediator import Mediator


@lru_cache(1)
def init_container() -> Container:
    return _initialize_container()


def _initialize_container() -> Container:
    container = Container()

    # init services

    # Handlers
    container.register(LoginPageCommandHandler)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        # command handlers
        # user app
        configure_login_page_handler = LoginPageCommandHandler()

        # commands
        # user app
        mediator.register_command(
            LoginPageCommand,
            [configure_login_page_handler],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
