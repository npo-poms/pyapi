from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(slots=True)
class CollectionType:
    class Meta:
        name = "collectionType"

    otherElement: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+(\.[0-9]+(\.[0-9]+)?)?",
        }
    )


@dataclass(slots=True)
class Collection(CollectionType):
    class Meta:
        name = "collection"
