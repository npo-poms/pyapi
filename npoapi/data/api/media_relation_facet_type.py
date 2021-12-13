from dataclasses import dataclass, field
from typing import Optional
from .extended_media_facet_type import ExtendedMediaFacetType
from .media_relation_search_type import MediaRelationSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaRelationFacetType(ExtendedMediaFacetType):
    class Meta:
        name = "mediaRelationFacetType"

    sub_search: Optional[MediaRelationSearchType] = field(
        default=None,
        metadata={
            "name": "subSearch",
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
