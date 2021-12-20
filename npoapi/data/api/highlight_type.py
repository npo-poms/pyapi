from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class HighlightType:
    class Meta:
        name = "highlightType"

    body: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    term: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
