from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class LiveItemize1:
    class Meta:
        name = "liveItemize"

    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    stream: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
