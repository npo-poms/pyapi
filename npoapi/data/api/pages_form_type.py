from dataclasses import dataclass, field
from typing import Optional
from .media_form import MediaForm
from .page_sort_list_type import PageSortListType
from .pages_facets_type import PagesFacetsType
from .pages_search_type import PagesSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PagesFormType:
    class Meta:
        name = "pagesFormType"

    searches: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sortFields: Optional[PageSortListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: Optional[PagesFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mediaForm: Optional[MediaForm] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
