from dataclasses import dataclass


@dataclass(frozen=True)
class Track:
    """One entry in a playlist. All data in this project is made up."""

    id: int
    title: str
    artist: str
    seconds: int
