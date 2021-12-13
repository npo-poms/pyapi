from dataclasses import dataclass
from .topicbandg_type import TopicbandgType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Topicbandg(TopicbandgType):
    class Meta:
        name = "topicbandg"
        namespace = "urn:vpro:gtaa:2017"
