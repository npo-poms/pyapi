from dataclasses import dataclass, field
from typing import Optional
from .text_facet_type import TextFacetType
from .title_search_type import TitleSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaTitleFacetType(TextFacetType):
    class Meta:
        name = "mediaTitleFacetType"

    subSearch: Optional[TitleSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
