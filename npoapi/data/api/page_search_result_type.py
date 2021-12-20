from dataclasses import dataclass, field
from typing import Optional
from .media_facets_result_type import MediaFacetsResultType
from .page_facets_result_type import PageFacetsResultType
from .search_result_type import SearchResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageSearchResultType(SearchResultType):
    class Meta:
        name = "pageSearchResultType"

    facets: Optional[PageFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    selectedFacets: Optional[PageFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mediaFacets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mediaSelectedFacets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
