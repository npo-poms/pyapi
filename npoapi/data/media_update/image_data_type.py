from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ImageDataType:
    class Meta:
        name = "imageDataType"

    data: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "format": "base64",
        }
    )
