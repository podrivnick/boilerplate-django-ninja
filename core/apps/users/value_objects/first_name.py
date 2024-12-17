import re
from dataclasses import dataclass

from core.apps.common.domain.base import ValueObject
from core.apps.common.utils.spec import IsStringSpec
from core.apps.common.utils.validators import IsNotEmptySpec


MAX_FIRSTNAME_LENGTH = 50
FIRSTNAME_PATTERN = re.compile(r"^[A-Z][a-zA-Z'-]*$")


@dataclass(frozen=True, eq=False)
class FirstName(ValueObject[str | None]):
    value: str | None

    def validate(self) -> None:
        first_name_spec = IsStringSpec().and_spec(IsNotEmptySpec())

        first_name_spec.is_satisfied(self.value)

    def exists(self) -> bool:
        return self.value is not None
