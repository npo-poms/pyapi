from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .transcode_status_enum import TranscodeStatusEnum

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class TranscodeStatusType:
    class Meta:
        name = "transcodeStatusType"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
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
    status_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusMessage",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    workflow_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "workflowType",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    workflow_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "workflowId",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "updateTime",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endTime",
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
    missing_media: Optional[bool] = field(
        default=None,
        metadata={
            "name": "missingMedia",
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
