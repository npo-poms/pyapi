from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class IntegerRangeValueType:
    class Meta:
        name = "integerRangeValueType"

    value: Optional[int] = field(
        default=None,
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
