from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class PortalRestrictionUpdateType:
    class Meta:
        name = "portalRestrictionUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
