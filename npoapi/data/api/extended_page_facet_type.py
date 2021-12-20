from dataclasses import dataclass, field
from typing import Optional
from .pages_search_type import PagesSearchType
from .text_facet_type import TextFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ExtendedPageFacetType(TextFacetType):
    class Meta:
        name = "extendedPageFacetType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    caseSensitive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
