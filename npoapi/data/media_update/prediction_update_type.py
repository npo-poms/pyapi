from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ..media.encryption import Encryption
from ..media.platform_type_enum import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class PredictionUpdateType:
    class Meta:
        name = "predictionUpdateType"

    value: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "required": True,
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
    encryption: Optional[Encryption] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
