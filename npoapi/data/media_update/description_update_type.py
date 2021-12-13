from dataclasses import dataclass, field
from typing import Optional
from ..media.textual_type_enum import TextualTypeEnum

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class DescriptionUpdateType:
    class Meta:
        name = "descriptionUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
