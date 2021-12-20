from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ErrorType:
    class Meta:
        name = "errorType"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    classValue: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    cause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    otherElement: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    testResult: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
