from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class TopicUpdateType:
    class Meta:
        name = "topicUpdateType"

    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
            "required": True,
        }
    )
