from dataclasses import (
    dataclass,
    field,
)
from typing import Optional

from core.infrastructure.exceptions.base import DomainException


@dataclass(frozen=True, eq=False)
class DataContainsNotOnlyDigitsException(DomainException):
    exception: Optional[str] = field(
        default="Data contains not only digits error.",
    )

    @property
    def message(self) -> Optional[str]:
        return self.exception


@dataclass(frozen=True, eq=False)
class DataIsEmptyException(DomainException):
    exception: Optional[str] = field(
        default="Data is empty.",
    )

    @property
    def message(self) -> Optional[str]:
        return self.exception
