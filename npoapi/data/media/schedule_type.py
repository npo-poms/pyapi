from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from .channel_enum import ChannelEnum
from .schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ScheduleType:
    class Meta:
        name = "scheduleType"

    scheduleEvent: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    releaseVersion: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    reruns: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
