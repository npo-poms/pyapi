from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .asset_data_type import AssetDataType
from .asset_location_type import AssetLocationType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class AssetType:
    class Meta:
        name = "assetType"

    assetData: Optional[AssetDataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    assetLocation: Optional[AssetLocationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
