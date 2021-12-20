from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class RelationType:
    class Meta:
        name = "relationType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    uriRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
