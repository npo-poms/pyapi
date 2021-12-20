from dataclasses import dataclass, field
from typing import Optional
from .match import Match

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class RangeMatcherType:
    class Meta:
        name = "rangeMatcherType"

    inclusiveEnd: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
