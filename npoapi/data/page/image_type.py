from dataclasses import dataclass, field
from typing import Optional
from ..shared.image_type_enum import ImageTypeEnum
from ..shared.license_enum import LicenseEnum

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class ImageType:
    class Meta:
        name = "imageType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    source_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    type: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
