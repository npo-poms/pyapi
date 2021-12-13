from dataclasses import dataclass, field
from typing import List
from .abstract_facet_type import AbstractFacetType
from .duration_range_facet_item_type import DurationRangeFacetItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DurationRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "durationRangeFacetsType"

    interval_or_range: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "interval",
                    "type": str,
                    "namespace": "urn:vpro:api:2013",
                },
                {
                    "name": "range",
                    "type": DurationRangeFacetItemType,
                    "namespace": "urn:vpro:api:2013",
                },
            ),
        }
    )
