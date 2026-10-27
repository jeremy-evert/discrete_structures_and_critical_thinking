from dataclasses import dataclass
from typing import Optional

from merger.names import same_person


@dataclass(frozen=True)
class Record:
    id: int
    name: str
    email: Optional[str] = None


def is_duplicate(a, b):
    """First draft: same person, and a's email matches b's (a missing email matches anything)."""
    return same_person(a.name, b.name) and (a.email is None or a.email == b.email)
