from dataclasses import dataclass, field
from typing import List
from .topic_update_type import TopicUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class TopicsUpdateType:
    class Meta:
        name = "topicsUpdateType"

    topic: List[TopicUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
