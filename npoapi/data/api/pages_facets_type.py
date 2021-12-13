from dataclasses import dataclass, field
from typing import Optional
from .date_range_facets_type import DateRangeFacetsType
from .extended_page_facet_type import ExtendedPageFacetType
from .page_facet_type import PageFacetType
from .page_relation_facet_list_type import PageRelationFacetListType
from .page_searchable_term_facet_type import PageSearchableTermFacetType
from .pages_search_type import PagesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PagesFacetsType:
    class Meta:
        name = "pagesFacetsType"

    sort_dates: Optional[DateRangeFacetsType] = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    types: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedPageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    keywords: Optional[ExtendedPageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[PageSearchableTermFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    portals: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sections: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[PageRelationFacetListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
