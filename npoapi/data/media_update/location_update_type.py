from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .av_atribute_update_type import AvAtributeUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class LocationUpdateType:
    class Meta:
        name = "locationUpdateType"

    program_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "programUrl",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    av_attributes: Optional[AvAtributeUpdateType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
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
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
