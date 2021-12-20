from dataclasses import dataclass, field
from typing import List, Optional
from .gtaa_status_type import GtaaStatusType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class TopicType:
    class Meta:
        name = "topicType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gtaaStatus: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
