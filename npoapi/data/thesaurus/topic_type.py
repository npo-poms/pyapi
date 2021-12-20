from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class TopicType:
    class Meta:
        name = "topicType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirectedFrom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    lastModified: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
