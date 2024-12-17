from functools import lru_cache

from punq import (
    Container,
    Scope,
)

from core.apps.main.repositories.main import ORMQueryProductRepository
from core.apps.main.services.main.base import BaseProductsService
from core.apps.main.services.main.main import (
    ORMCategoriesService,
    ORMProductsService,
)
from core.apps.main.services.universal import (
    ORMAllProductsService,
    ORMFavoriteProductsIdsService,
)
from core.apps.main.use_cases.main import (
    MainPageCommand,
    MainPageCommandHandler,
)
from core.infrastructure.mediator.mediator import Mediator


@lru_cache(1)
def init_container() -> Container:
    return _initialize_container()


def _initialize_container() -> Container:
    container = Container()

    # init services
    def init_product_service() -> BaseProductsService:
        return ORMProductsService(
            query_product_repository=ORMQueryProductRepository(),
        )

    container.register(
        BaseProductsService,
        factory=init_product_service,
        scope=Scope.singleton,
    )

    # Handlers
    container.register(MainPageCommandHandler)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        # command handlers
        # main app
        configure_main_page_handler = MainPageCommandHandler(
            favorite_products_service_ids=ORMFavoriteProductsIdsService(),
            get_all_products_service=ORMAllProductsService(),
            categories_service=ORMCategoriesService(),
            products_service=container.resolve(
                BaseProductsService,
            ),
        )

        # commands
        # main app
        mediator.register_command(
            MainPageCommand,
            [configure_main_page_handler],
        )

        return mediator

    container.register(Mediator, factory=init_mediator)

    return container
