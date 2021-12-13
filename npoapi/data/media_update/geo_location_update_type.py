from dataclasses import dataclass, field
from typing import Optional
from ..media.geo_role_type import GeoRoleType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class GeoLocationUpdateType:
    class Meta:
        name = "geoLocationUpdateType"

    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
