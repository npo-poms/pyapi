from dataclasses import dataclass, field
from typing import List, Optional
from .media_type_enum import MediaTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class RecursiveMemberRef:
    class Meta:
        name = "recursiveMemberRef"

    memberOf: List["RecursiveMemberRef"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    episodeOf: List["RecursiveMemberRef"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segmentOf: Optional["RecursiveMemberRef"] = field(
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
