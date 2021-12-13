from dataclasses import dataclass, field
from typing import List, Optional
from ..media.program_type_enum import ProgramTypeEnum
from .media_update_type import MediaUpdateType
from .member_ref_update_type import MemberRefUpdateType
from .segment import Segment

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ProgramUpdateType(MediaUpdateType):
    """
    :ivar episode_of: episodeOf works similar to memberOf. Important differences: only programs of type CLIP or
        BROADCAST can be an episode of a group and the group can only be of type SERIES or SEASON.
    :ivar segments: Optional list of program segments. A segment is a part of a program that can be visually
        shown on the timeline of a player. A segment always has a start time indicating the start of the segment
        relative to the parent program. A segment can have the same fields as other media objects, like titles,
        descriptions, images, locations, etc. The standard scenario when playing a segment is to load a location
        of the parent media object and to use the start time as an offset to start playing the segment. However,
        it is also possible for a segment to have its own locations. This makes it possible to for instance have
        a podcast of a weekly segment in a radio show without providing the complete radio program it is a part
        of. Rules: - Start time is required - If duration is not set the player should play until the end of the
        program - Removing a program also deletes its segments
    :ivar type:
    """
    class Meta:
        name = "programUpdateType"

    episode_of: List[MemberRefUpdateType] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    segments: Optional["ProgramUpdateType.Segments"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    type: Optional[ProgramTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class Segments:
        segment: List[Segment] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )
