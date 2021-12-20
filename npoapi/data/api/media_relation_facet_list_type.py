from dataclasses import dataclass, field
from typing import List, Optional
from .abstract_facet_type import AbstractFacetType
from .media_relation_facet_type import MediaRelationFacetType
from .media_relation_search_type import MediaRelationSearchType
from .media_search_type import MediaSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "mediaRelationFacetListType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    subSearch: Optional[MediaRelationSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facet: List[MediaRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
