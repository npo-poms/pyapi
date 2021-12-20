from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class GenreType:
    class Meta:
        name = "genreType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    displayName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
