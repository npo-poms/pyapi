from dataclasses import dataclass
from .location_update_type import LocationUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Location(LocationUpdateType):
    class Meta:
        name = "location"
        namespace = "urn:vpro:media:update:2009"
