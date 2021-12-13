from dataclasses import dataclass
from .topic_type import TopicType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Topic(TopicType):
    class Meta:
        name = "topic"
        namespace = "urn:vpro:gtaa:2017"
