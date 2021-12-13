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
    selected_facets: Optional[PageFacetsResultType] = field(
        default=None,
        metadata={
            "name": "selectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "name": "mediaFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    media_selected_facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "name": "mediaSelectedFacets",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
