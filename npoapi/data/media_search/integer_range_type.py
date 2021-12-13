from dataclasses import dataclass, field
from typing import Optional
from .integer_range_value_type import IntegerRangeValueType

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class IntegerRangeType:
    class Meta:
        name = "integerRangeType"

    start: Optional[IntegerRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    stop: Optional[IntegerRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
