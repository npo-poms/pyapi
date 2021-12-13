from dataclasses import dataclass, field
from typing import Optional
from ..media.role_type import RoleType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class NameUpdateType:
    class Meta:
        name = "nameUpdateType"

    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
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
