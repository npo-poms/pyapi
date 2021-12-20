from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .transcode_status_enum import TranscodeStatusEnum

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class TranscodeStatusType:
    class Meta:
        name = "transcodeStatusType"

    fileName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    status: Optional[TranscodeStatusEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    statusMessage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    workflowType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    workflowId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    startTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    updateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    endTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    broadcasters: Optional["TranscodeStatusType.Broadcasters"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    missingMedia: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Broadcasters:
        broadcaster: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )
