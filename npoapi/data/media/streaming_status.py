from dataclasses import dataclass, field
from typing import Optional
from .streaming_status_value import StreamingStatusValue

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class StreamingStatus:
    class Meta:
        name = "streamingStatus"
        namespace = "urn:vpro:media:2009"

    withDrm: Optional[StreamingStatusValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    withoutDrm: Optional[StreamingStatusValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
