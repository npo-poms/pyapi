from dataclasses import dataclass, field
from typing import List, Optional
from .media_facets_type import MediaFacetsType
from .media_search_type import MediaSearchType
from .media_sort_type import MediaSortType
from .title_sort_order_type import TitleSortOrderType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFormType:
    class Meta:
        name = "mediaFormType"

    searches: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sortFields: Optional["MediaFormType.SortFields"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: Optional[MediaFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class SortFields:
        sortOrTitleSort: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "sort",
                        "type": MediaSortType,
                        "namespace": "urn:vpro:api:2013",
                    },
                    {
                        "name": "titleSort",
                        "type": TitleSortOrderType,
                        "namespace": "urn:vpro:api:2013",
                    },
                ),
            }
        )
