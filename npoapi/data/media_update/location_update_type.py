from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .av_atribute_update_type import AvAtributeUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class LocationUpdateType:
    class Meta:
        name = "locationUpdateType"

    programUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    avAttributes: Optional[AvAtributeUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
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
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
