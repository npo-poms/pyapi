from dataclasses import dataclass, field
from typing import Optional
from .page_facet_type import PageFacetType
from .term_search_type import TermSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageSearchableTermFacetType(PageFacetType):
    class Meta:
        name = "pageSearchableTermFacetType"

    subSearch: Optional[TermSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
