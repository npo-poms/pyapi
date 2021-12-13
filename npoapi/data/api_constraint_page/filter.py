from dataclasses import dataclass, field
from typing import Optional
from .or_mod import (
    And,
    Or,
)

__NAMESPACE__ = "urn:vpro:api:constraint:page:2013"


@dataclass
class Filter:
    class Meta:
        name = "filter"
        namespace = "urn:vpro:api:constraint:page:2013"

    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        }
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    portal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    section: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    genre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
