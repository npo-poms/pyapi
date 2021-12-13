from dataclasses import dataclass
from .schedule_form_type import ScheduleFormType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ScheduleForm(ScheduleFormType):
    class Meta:
        name = "scheduleForm"
        namespace = "urn:vpro:api:2013"
