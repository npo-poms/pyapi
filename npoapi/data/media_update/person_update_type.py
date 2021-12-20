from dataclasses import dataclass, field
from typing import Optional
from ..media.role_type import RoleType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class PersonUpdateType:
    class Meta:
        name = "personUpdateType"

    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
