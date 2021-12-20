from dataclasses import dataclass, field
from typing import List
from .abstract_facet_type import AbstractFacetType
from .date_range_facet_item_type import DateRangeFacetItemType
from .date_range_preset_type_enum import DateRangePresetTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class DateRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "dateRangeFacetsType"

    intervalOrPresetOrRange: List[object] = field(
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
                    "name": "preset",
                    "type": DateRangePresetTypeEnum,
                    "namespace": "urn:vpro:api:2013",
                },
                {
                    "name": "range",
                    "type": DateRangeFacetItemType,
                    "namespace": "urn:vpro:api:2013",
                },
            ),
        }
    )
