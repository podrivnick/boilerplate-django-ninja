from dataclasses import (
    dataclass,
    field,
)
from typing import Optional

from core.api.v1.base_dto import BaseDTOAPI


@dataclass(frozen=True, eq=False)
class DTOResponseLoginAPI(BaseDTOAPI):
    username: Optional[str] | None = field(default=None)
    email: Optional[str] | None = field(default=None)
    password: Optional[str] | None = field(default=None)


@dataclass(frozen=True, eq=False)
class DTOResponseAuthenticateAPI(BaseDTOAPI):
    username: str | None = field(default=None)
    email: str | None = field(default=None)
    password: str | None = field(default=None)
    session_key: str | bool = field(default=False)
    is_authenticated: bool = field(default=False)


@dataclass(frozen=True, eq=False)
class DTOResponseLogoutPageAPI(BaseDTOAPI):
    username: str | None = field(default=None)
    is_authenticated: bool = field(default=False)
