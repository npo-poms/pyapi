from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class HasLocationConstraintType:
    class Meta:
        name = "hasLocationConstraintType"

    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
