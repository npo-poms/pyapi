from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from ..media.segment_type_enum import SegmentTypeEnum
from .media_update_type import MediaUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class SegmentUpdateType(MediaUpdateType):
    class Meta:
        name = "segmentUpdateType"

    start: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    midRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[SegmentTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
