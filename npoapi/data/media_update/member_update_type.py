from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class MemberUpdateType:
    class Meta:
        name = "memberUpdateType"

    anyElement: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
