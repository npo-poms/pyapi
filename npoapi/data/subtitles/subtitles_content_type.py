from dataclasses import dataclass, field
from typing import Optional
from .subtitles_format_enum import SubtitlesFormatEnum

__NAMESPACE__ = "urn:vpro:media:subtitles:2009"


@dataclass
class SubtitlesContentType:
    class Meta:
        name = "subtitlesContentType"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    format: Optional[SubtitlesFormatEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    charset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
