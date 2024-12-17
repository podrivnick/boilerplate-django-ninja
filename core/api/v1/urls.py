from ninja import Router

from core.api.v1.users.handlers import router as user_router


router = Router(tags=["v1"])

router.add_router("", user_router, tags=["user"])
