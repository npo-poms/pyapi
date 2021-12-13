from dataclasses import dataclass, field
from typing import Optional
from ..media.platform_type_enum import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class HasPredictionConstraintType:
    class Meta:
        name = "hasPredictionConstraintType"

    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
