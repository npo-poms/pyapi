from dataclasses import dataclass, field
from typing import List
from .matcher_list import MatcherList
from .text_matcher_type import TextMatcherType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class TextMatcherListType(MatcherList):
    class Meta:
        name = "textMatcherListType"

    matcher: List[TextMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
