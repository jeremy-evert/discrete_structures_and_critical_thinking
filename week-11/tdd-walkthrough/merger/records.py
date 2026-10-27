from dataclasses import dataclass
from typing import Optional

from merger.names import same_person


@dataclass(frozen=True)
class Record:
    id: int
    name: str
    email: Optional[str] = None


def is_duplicate(a, b):
    """Same person and same email. Written so swapping a and b cannot change the answer."""
    return same_person(a.name, b.name) and a.email == b.email
