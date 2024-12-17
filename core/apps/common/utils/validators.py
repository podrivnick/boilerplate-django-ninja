import re
from dataclasses import (
    dataclass,
    field,
)
from typing import Pattern

from core.apps.common.exceptions.spec import DataIsEmptyException
from core.apps.common.utils.spec import Specification
from core.apps.users.exceptions.main import (
    IncorrectFormatEmailException,
    IncorrectFormatPhoneException,
)


# not empty  noqa
@dataclass(frozen=True)
class IsNotEmptySpec(Specification):
    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if not bool(item.strip()):
            raise DataIsEmptyException()
        return True


@dataclass(frozen=True)
class IsValidEmailSpec(Specification):
    _email_pattern: Pattern[str] = field(
        default_factory=lambda: re.compile(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        ),
    )

    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if not re.match(
            self._email_pattern,
            item,
        ):
            raise IncorrectFormatEmailException()
        return True


@dataclass(frozen=True)
class IsValidPhoneSpec(Specification):
    _phone_pattern: Pattern[str] = field(
        default_factory=lambda: re.compile(r"^\+?[1-9]\d{9,14}$"),
    )

    def is_satisfied(
        self,
        item: str,
    ) -> bool:
        if not re.match(
            self._phone_pattern,
            item,
        ):
            raise IncorrectFormatPhoneException()
        return True
