from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ..shared.owner_type_enum import OwnerTypeEnum
from ..shared.subtitles_type_enum import SubtitlesTypeEnum
from ..shared.subtitles_workflow_enum import SubtitlesWorkflowEnum
from .subtitles_content_type import SubtitlesContentType

__NAMESPACE__ = "urn:vpro:media:subtitles:2009"


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
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Attribute",
        }
    )
    last_modified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModified",
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
    cue_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "cueCount",
            "type": "Attribute",
        }
    )
