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

    asset_data: Optional[AssetDataType] = field(
        default=None,
        metadata={
            "name": "assetData",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    asset_location: Optional[AssetLocationType] = field(
        default=None,
        metadata={
            "name": "assetLocation",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
