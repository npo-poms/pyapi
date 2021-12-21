from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:api:constraint:2014"


@dataclass
class LocalizedString:
    class Meta:
        name = "localizedString"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


class OperatorType(Enum):
    LT = "LT"
    GT = "GT"
    EQ = "EQ"
    LTE = "LTE"
    GTE = "GTE"


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


@dataclass
class NotPredicateTestResult:
    class Meta:
        name = "notPredicateTestResult"

    description: Optional[LocalizedString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:2014",
        }
    )
    clause: Optional[object] = field(
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


@dataclass
class AndPredicateTestResult(BooleanPredicateTestResult):
    class Meta:
        name = "andPredicateTestResult"


@dataclass
class OrPredicateTestResult(BooleanPredicateTestResult):
    class Meta:
        name = "orPredicateTestResult"
