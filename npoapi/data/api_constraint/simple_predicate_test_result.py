from dataclasses import dataclass, field
from typing import Optional
from .localized_string import LocalizedString

__NAMESPACE__ = "urn:vpro:api:constraint:2014"


@dataclass
class SimplePredicateTestResult:
    class Meta:
        name = "simplePredicateTestResult"

    description: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:2014",
        }
    )
    applies: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
