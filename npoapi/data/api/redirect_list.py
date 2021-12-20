from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .redirect_entry import RedirectEntry

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class RedirectList:
    class Meta:
        name = "redirectList"

    entry: List[RedirectEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    lastUpdate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
