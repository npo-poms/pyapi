from dataclasses import dataclass, field
from typing import List
from .page_sort_type import PageSortType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageSortListType:
    class Meta:
        name = "pageSortListType"

    sort: List[PageSortType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
