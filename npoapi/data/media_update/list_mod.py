from dataclasses import dataclass, field
from typing import Optional
from .list_order import ListOrder

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ListType:
    class Meta:
        name = "list"
        namespace = "urn:vpro:media:update:2009"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    total_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalCount",
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    order: Optional[ListOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
