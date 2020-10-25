from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from npoapi.data.shared import (
    OwnerTypeEnum,
    SubtitlesTypeEnum,
    SubtitlesWorkflowEnum,
)

__NAMESPACE__ = "urn:vpro:media:subtitles:2009"


class SubtitlesFormatEnum(Enum):
    """
    :cvar WEBVTT:
    :cvar TT888:
    :cvar EBU:
    :cvar SRT:
    """
    WEBVTT = "WEBVTT"
    TT888 = "TT888"
    EBU = "EBU"
    SRT = "SRT"


@dataclass
class SubtitlesContentType:
    """
    :ivar value:
    :ivar format:
    :ivar charset:
    """
    class Meta:
        name = "subtitlesContentType"

    value: Optional[str] = field(
        default=None,
    )
    format: Optional[SubtitlesFormatEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    charset: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class SubtitlesType:
    """
    :ivar content:
    :ivar mid:
    :ivar offset:
    :ivar creation_date:
    :ivar last_modified:
    :ivar type:
    :ivar lang:
    :ivar owner:
    :ivar workflow:
    :ivar cue_count:
    """
    class Meta:
        name = "subtitlesType"

    content: Optional[SubtitlesContentType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:media:subtitles:2009",
            required=True
        )
    )
    mid: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    offset: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="creationDate",
            type="Attribute"
        )
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lastModified",
            type="Attribute"
        )
    )
    type: Optional[SubtitlesTypeEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    lang: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    workflow: Optional[SubtitlesWorkflowEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    cue_count: Optional[int] = field(
        default=None,
        metadata=dict(
            name="cueCount",
            type="Attribute"
        )
    )


@dataclass
class Subtitles(SubtitlesType):
    class Meta:
        name = "subtitles"
        namespace = "urn:vpro:media:subtitles:2009"
