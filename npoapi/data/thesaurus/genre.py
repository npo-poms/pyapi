from dataclasses import dataclass
from .genre_type import GenreType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Genre(GenreType):
    class Meta:
        name = "genre"
        namespace = "urn:vpro:gtaa:2017"
