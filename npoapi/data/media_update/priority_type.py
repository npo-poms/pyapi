from enum import Enum

__NAMESPACE__ = "urn:vpro:media:update:2009"


class PriorityType(Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    URGENT = "URGENT"
