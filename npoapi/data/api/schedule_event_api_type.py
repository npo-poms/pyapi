from dataclasses import dataclass, field
from typing import Optional
from ..media.group import Group
from ..media.program import Program
from ..media.schedule_event_type import ScheduleEventType
from ..media.segment import Segment

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ScheduleEventApiType(ScheduleEventType):
    class Meta:
        name = "scheduleEventApiType"

    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment: Optional[Segment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
