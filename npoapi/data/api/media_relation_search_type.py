from dataclasses import dataclass, field
from typing import Optional
from .extended_text_matcher_list_type import ExtendedTextMatcherListType
from .match import Match
from .text_matcher_list_type import TextMatcherListType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaRelationSearchType:
    class Meta:
        name = "mediaRelationSearchType"

    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    values: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    uriRefs: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
