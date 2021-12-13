from dataclasses import dataclass, field
from typing import Optional
from .media_search_type import MediaSearchType
from .text_facet_type import TextFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFacetType(TextFacetType):
    class Meta:
        name = "mediaFacetType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
