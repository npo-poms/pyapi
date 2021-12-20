from dataclasses import dataclass, field
from typing import List, Optional
from .total_qualifier import TotalQualifier

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ResultType:
    class Meta:
        name = "resultType"

    items: Optional["ResultType.Items"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    total: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    totalQualifier: Optional[TotalQualifier] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Items:
        item: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )
