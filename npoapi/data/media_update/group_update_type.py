from dataclasses import dataclass, field
from typing import Optional
from ..media.group_type_enum import GroupTypeEnum
from .media_update_type import MediaUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class GroupUpdateType(MediaUpdateType):
    class Meta:
        name = "groupUpdateType"

    poSeriesId: Optional[str] = field(
        default=None,
        metadata={
            "name": "poSeriesID",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    type: Optional[GroupTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
