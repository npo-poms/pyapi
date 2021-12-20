from dataclasses import dataclass, field
from typing import Optional
from .image_location_type import ImageLocationType
from ..shared.image_type_enum import ImageTypeEnum
from ..shared.license_enum import LicenseEnum

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class ImageUpdateType:
    class Meta:
        name = "imageUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    sourceName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    imageLocation: Optional[ImageLocationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    type: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
