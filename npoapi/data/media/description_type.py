from dataclasses import dataclass, field
from typing import Optional
from .textual_type_enum import TextualTypeEnum
from ..shared.owner_type_enum import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class DescriptionType:
    class Meta:
        name = "descriptionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
