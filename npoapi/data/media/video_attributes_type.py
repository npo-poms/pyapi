from dataclasses import dataclass, field
from typing import Optional
from .aspect_ratio_enum import AspectRatioEnum
from .color_type import ColorType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class VideoAttributesType:
    """
    :ivar color:
    :ivar videoCoding:
    :ivar aspectRatio:
    :ivar height:
    :ivar heigth: This obviously is a typo.
    :ivar width:
    """
    class Meta:
        name = "videoAttributesType"

    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    videoCoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    aspectRatio: Optional[AspectRatioEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    heigth: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
