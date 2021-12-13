from dataclasses import dataclass, field
from typing import Optional
from .match import Match
from .simple_match_type import SimpleMatchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class SimpleMatcherType:
    """
    :ivar value:
    :ivar fuzziness:
    :ivar semantic: Whether the search must happen via the semantic vectorization. This is beta feature, which
        may not be enabled.
    :ivar match_type:
    :ivar match:
    """
    class Meta:
        name = "simpleMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    fuzziness: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    semantic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match_type: Optional[SimpleMatchType] = field(
        default=None,
        metadata={
            "name": "matchType",
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
