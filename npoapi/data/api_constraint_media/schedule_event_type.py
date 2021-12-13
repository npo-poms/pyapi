from dataclasses import dataclass, field
from typing import Optional
from ..api_constraint.operator_type import OperatorType

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class ScheduleEventType:
    """
    documentation for schedule event date.

    :ivar date: A timestamp spec. This is parsed by the natty parser. Try out with
        http://natty.joestelmach.com/try.jsp
    :ivar operator:
    """
    class Meta:
        name = "scheduleEventType"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    operator: Optional[OperatorType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
