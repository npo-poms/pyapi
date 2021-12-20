from dataclasses import dataclass, field
from typing import List
from .page_relation_search_type import PageRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageRelationSearchListType:
    class Meta:
        name = "pageRelationSearchListType"

    relationSearch: List[PageRelationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
