from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class RelationUpdateType:
    class Meta:
        name = "relationUpdateType"

    value: str = field(
        default="",
        metadata={
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
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uriRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
