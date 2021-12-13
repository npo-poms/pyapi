from dataclasses import dataclass, field
from typing import Optional
from .pages_search_type import PagesSearchType
from .text_facet_type import TextFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageFacetType(TextFacetType):
    class Meta:
        name = "pageFacetType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
