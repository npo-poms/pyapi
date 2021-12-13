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
    byte_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "byteSize",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    av_file_format: Optional[AvFileFormatEnum] = field(
        default=None,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    video_attributes: Optional[VideoAttributesUpdateType] = field(
        default=None,
        metadata={
            "name": "videoAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    audio_attributes: Optional[AudioAttributesUpdateType] = field(
        default=None,
        metadata={
            "name": "audioAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
