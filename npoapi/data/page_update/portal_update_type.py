from dataclasses import dataclass, field
from typing import Optional
from ..page.section_type import SectionType

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class PortalUpdateType:
    class Meta:
        name = "portalUpdateType"

    section: Optional[SectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
