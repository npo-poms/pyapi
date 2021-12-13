from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ..media.geo_restriction_enum import GeoRestrictionEnum
from ..media.platform_type_enum import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class GeoRestrictionUpdateType:
    class Meta:
        name = "geoRestrictionUpdateType"

    value: Optional[GeoRestrictionEnum] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
