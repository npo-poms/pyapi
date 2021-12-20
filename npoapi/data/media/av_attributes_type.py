from dataclasses import dataclass, field
from typing import Optional
from .audio_attributes_type import AudioAttributesType
from .av_file_format_enum import AvFileFormatEnum
from .video_attributes_type import VideoAttributesType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class AvAttributesType:
    class Meta:
        name = "avAttributesType"

    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    byteSize: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    avFileFormat: Optional[AvFileFormatEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    videoAttributes: Optional[VideoAttributesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    audioAttributes: Optional[AudioAttributesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
