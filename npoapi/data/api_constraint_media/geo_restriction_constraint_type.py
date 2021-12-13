from dataclasses import dataclass, field
from typing import Optional
from ..media.platform_type_enum import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class GeoRestrictionConstraintType:
    class Meta:
        name = "geoRestrictionConstraintType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
