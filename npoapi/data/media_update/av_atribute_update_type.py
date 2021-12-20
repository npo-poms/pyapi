from dataclasses import dataclass, field
from typing import Optional
from ..media.av_file_format_enum import AvFileFormatEnum
from .audio_attributes_update_type import AudioAttributesUpdateType
from .video_attributes_update_type import VideoAttributesUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class AvAtributeUpdateType:
    class Meta:
        name = "avAtributeUpdateType"

    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    byteSize: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    avFileFormat: Optional[AvFileFormatEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    videoAttributes: Optional[VideoAttributesUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    audioAttributes: Optional[AudioAttributesUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
