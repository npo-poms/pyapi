from dataclasses import dataclass, field
from typing import Optional
from ..media.aspect_ratio_enum import AspectRatioEnum
from ..media.color_type import ColorType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class VideoAttributesUpdateType:
    class Meta:
        name = "videoAttributesUpdateType"

    aspect_ratio: Optional[AspectRatioEnum] = field(
        default=None,
        metadata={
            "name": "aspectRatio",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    coding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
