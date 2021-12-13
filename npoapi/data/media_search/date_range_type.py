from dataclasses import dataclass, field
from typing import Optional
from .date_range_value_type import DateRangeValueType

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class DateRangeType:
    class Meta:
        name = "dateRangeType"

    start: Optional[DateRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    stop: Optional[DateRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
