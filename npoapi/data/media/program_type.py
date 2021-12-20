from dataclasses import dataclass, field
from typing import List, Optional
from .base_media_type import BaseMediaType
from .member_ref_type import MemberRefType
from .program_type_enum import ProgramTypeEnum
from .schedule_events_type import ScheduleEventsType
from .segments_type import SegmentsType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ProgramType(BaseMediaType):
    """
    :ivar scheduleEvents:
    :ivar episodeOf: A program (only if its type is 'BROADCAST') can be an episode of a group of type 'SERIES' or
        'SEASON'.
    :ivar segments:
    :ivar type: The type of this program (e.g. BROADCAST, TRACK, CLIP)
    """
    class Meta:
        name = "programType"

    scheduleEvents: Optional[ScheduleEventsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    episodeOf: List[MemberRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segments: Optional[SegmentsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    type: Optional[ProgramTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
