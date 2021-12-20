from dataclasses import dataclass, field
from typing import Optional
from .base_media_type import BaseMediaType
from .group_type_enum import GroupTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GroupType(BaseMediaType):
    class Meta:
        name = "groupType"

    poSeriesId: Optional[str] = field(
        default=None,
        metadata={
            "name": "poSeriesID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    isOrdered: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[GroupTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    defaultElement: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
