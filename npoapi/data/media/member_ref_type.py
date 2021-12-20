from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .media_type_enum import MediaTypeEnum
from .recursive_member_ref import RecursiveMemberRef

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class MemberRefType:
    """
    :ivar episodeOf:
    :ivar memberOf:
    :ivar segmentOf:
    :ivar midRef: Reference to the MID of the parent of this object.
    :ivar urnRef: Reference to the URN of the parent of this object. URN's are no longer actively used, but the
        attribute is still available for backwards compatibility.
    :ivar cridRef: Reference to a crid of the parent of this object. This is only used for imports from systems
        that cannot supply a MID or URN. POMS does not export or publish parent crids.
    :ivar type:
    :ivar index:
    :ivar highlighted:
    :ivar added:
    """
    class Meta:
        name = "memberRefType"

    episodeOf: List[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    memberOf: List[RecursiveMemberRef] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segmentOf: Optional[RecursiveMemberRef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    midRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urnRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cridRef: Optional[str] = field(
        default=None,
        metadata={
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
