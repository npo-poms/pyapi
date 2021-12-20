from dataclasses import dataclass, field
from typing import Optional
from .media_facets_result_type import MediaFacetsResultType
from .search_result_type import SearchResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class GenericMediaSearchResultType(SearchResultType):
    class Meta:
        name = "genericMediaSearchResultType"

    facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    selectedFacets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
