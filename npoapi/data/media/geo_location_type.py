from dataclasses import dataclass, field
from typing import List, Optional
from .geo_role_type import GeoRoleType
from .gtaa_status_type import GtaaStatusType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GeoLocationType:
    class Meta:
        name = "geoLocationType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    scopeNote: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    role: Optional[GeoRoleType] = field(
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
