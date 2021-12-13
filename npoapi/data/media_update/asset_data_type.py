from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class AssetDataType:
    class Meta:
        name = "assetDataType"

    data: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "format": "base64",
        }
    )
