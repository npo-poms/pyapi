from dataclasses import dataclass, field
from typing import List, Optional
from .abstract_facet_type import AbstractFacetType
from .page_relation_facet_type import PageRelationFacetType
from .page_relation_search_type import PageRelationSearchType
from .pages_search_type import PagesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "pageRelationFacetListType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sub_search: Optional[PageRelationSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facet: List[PageRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
