from dataclasses import dataclass, field
from typing import List
from .extended_matcher_type import ExtendedMatcherType
from .matcher_list import MatcherList

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ExtendedTextMatcherListType(MatcherList):
    class Meta:
        name = "extendedTextMatcherListType"

    matcher: List[ExtendedMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
