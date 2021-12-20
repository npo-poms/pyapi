from dataclasses import dataclass, field
from typing import List
from .geo_location_update_type import GeoLocationUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class GeoLocationsUpdateType:
    class Meta:
        name = "geoLocationsUpdateType"

    geoLocation: List[GeoLocationUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
