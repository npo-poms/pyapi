from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .media_type_enum import MediaTypeEnum
from .recursive_member_ref import RecursiveMemberRef

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class MemberRefType:
    """
    :ivar episode_of:
    :ivar member_of:
    :ivar segment_of:
    :ivar mid_ref: Reference to the MID of the parent of this object.
    :ivar urn_ref: Reference to the URN of the parent of this object. URN's are no longer actively used, but the
        attribute is still available for backwards compatibility.
    :ivar crid_ref: Reference to a crid of the parent of this object. This is only used for imports from systems
        that cannot supply a MID or URN. POMS does not export or publish parent crids.
    :ivar type:
    :ivar index:
    :ivar highlighted:
    :ivar added:
    """
    class Meta:
        name = "memberRefType"

    episode_of: List[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    member_of: List[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment_of: Optional[RecursiveMemberRef] = field(
        default=None,
        metadata={
            "name": "segmentOf",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "urnRef",
            "type": "Attribute",
        }
    )
    crid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "cridRef",
            "type": "Attribute",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    added: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
