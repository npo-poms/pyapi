from dataclasses import dataclass, field
from typing import Optional
from .match import Match
from .standard_match_type import StandardMatchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TextMatcherType:
    class Meta:
        name = "textMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    matchType: Optional[StandardMatchType] = field(
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
