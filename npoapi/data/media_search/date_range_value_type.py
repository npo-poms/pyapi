from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class DateRangeValueType:
    class Meta:
        name = "dateRangeValueType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
