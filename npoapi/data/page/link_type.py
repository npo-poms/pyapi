from dataclasses import dataclass, field
from typing import Optional
from .link_type_enum import LinkTypeEnum

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class LinkType:
    class Meta:
        name = "linkType"

    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    pageRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[LinkTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
