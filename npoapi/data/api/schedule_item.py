from dataclasses import dataclass
from .schedule_event_api_type import ScheduleEventApiType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ScheduleItem(ScheduleEventApiType):
    class Meta:
        name = "scheduleItem"
        namespace = "urn:vpro:api:2013"
