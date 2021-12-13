from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CollectionType:
    class Meta:
        name = "collectionType"

    other_element: List[object] = field(
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
