from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .geo_restriction_enum import GeoRestrictionEnum
from .platform_type_enum import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class GeoRestrictionType:
    class Meta:
        name = "geoRestrictionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    regionId: Optional[GeoRestrictionEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
