from dataclasses import dataclass, field
from typing import List, Optional
from .localized_string import LocalizedString

__NAMESPACE__ = "urn:vpro:api:constraint:2014"


@dataclass
class BooleanPredicateTestResult:
    class Meta:
        name = "booleanPredicateTestResult"

    description: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:2014",
        }
    )
    clauses: Optional["BooleanPredicateTestResult.Clauses"] = field(
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

    @dataclass
    class Clauses:
        clause: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:constraint:2014",
            }
        )
