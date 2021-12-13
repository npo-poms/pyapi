from dataclasses import dataclass, field
from typing import List, Optional
from ..media.media_type_enum import MediaTypeEnum

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class MidAndTypeType:
    class Meta:
        name = "midAndTypeType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
