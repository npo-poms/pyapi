from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class MemberRefUpdateType:
    class Meta:
        name = "memberRefUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 4,
        }
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
