from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from npoapi.data.shared import (
    OwnerTypeEnum,
    SubtitlesTypeEnum,
    SubtitlesWorkflowEnum,
)

__NAMESPACE__ = "urn:vpro:media:subtitles:2009"


class SubtitlesFormatEnum(Enum):
    WEBVTT = "WEBVTT"
    TT888 = "TT888"
    EBU = "EBU"
    SRT = "SRT"


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


@dataclass
class SubtitlesType:
    class Meta:
        name = "subtitlesType"

    content: Optional[SubtitlesContentType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:subtitles:2009",
            "required": True,
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    creationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[SubtitlesTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    workflow: Optional[SubtitlesWorkflowEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cueCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Subtitles(SubtitlesType):
    class Meta:
        name = "subtitles"
        namespace = "urn:vpro:media:subtitles:2009"
