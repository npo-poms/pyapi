from dataclasses import dataclass, field
from typing import Optional
from .media_facet_type import MediaFacetType
from .member_ref_search_type import MemberRefSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MemberRefFacetType(MediaFacetType):
    class Meta:
        name = "memberRefFacetType"

    subSearch: Optional[MemberRefSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
