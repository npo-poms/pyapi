from dataclasses import dataclass
from .genre_type import GenreType

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class Genre(GenreType):
    class Meta:
        name = "genre"
        namespace = "urn:vpro:pages:2013"
