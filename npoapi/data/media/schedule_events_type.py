from dataclasses import dataclass, field
from typing import List
from .schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ScheduleEventsType:
    class Meta:
        name = "scheduleEventsType"

    scheduleEvent: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
