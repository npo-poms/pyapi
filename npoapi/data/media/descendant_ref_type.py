from dataclasses import dataclass, field
from typing import Optional
from .media_type_enum import MediaTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class DescendantRefType:
    class Meta:
        name = "descendantRefType"

    midRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urnRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
