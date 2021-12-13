from dataclasses import dataclass
from .page_search_result_type import PageSearchResultType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PageSearchResult(PageSearchResultType):
    class Meta:
        name = "pageSearchResult"
        namespace = "urn:vpro:api:2013"
