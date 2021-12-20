from dataclasses import dataclass, field
from typing import List, Optional
from .gtaa_status_type import GtaaStatusType
from .role_type import RoleType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class NameType:
    class Meta:
        name = "nameType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gtaaStatus: Optional[GtaaStatusType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
