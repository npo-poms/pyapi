from dataclasses import dataclass, field
from typing import Optional
from .gtaa_status_type import GtaaStatusType
from .role_type import RoleType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class PersonType:
    class Meta:
        name = "personType"

    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
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
