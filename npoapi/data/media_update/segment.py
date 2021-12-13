from dataclasses import dataclass
from .segment_update_type import SegmentUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Segment(SegmentUpdateType):
    class Meta:
        name = "segment"
        namespace = "urn:vpro:media:update:2009"
