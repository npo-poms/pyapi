from dataclasses import dataclass, field
from typing import List
from .term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaGenreFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "mediaGenreFacetResultItemType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
