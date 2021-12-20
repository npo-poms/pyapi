from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class EmbedUpdateType:
    class Meta:
        name = "embedUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    midRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
