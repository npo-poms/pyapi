from dataclasses import dataclass
from .live_itemize_1 import LiveItemize1

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Liveitemize(LiveItemize1):
    class Meta:
        name = "liveitemize"
        namespace = "urn:vpro:media:update:2009"
