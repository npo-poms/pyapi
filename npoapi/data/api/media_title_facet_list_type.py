from dataclasses import dataclass, field
from typing import List, Optional
from .media_facet_type import MediaFacetType
from .media_title_facet_type import MediaTitleFacetType
from .title_search_type import TitleSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaTitleFacetListType(MediaFacetType):
    class Meta:
        name = "mediaTitleFacetListType"

    subSearch: Optional[TitleSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    title: List[MediaTitleFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
