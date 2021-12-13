from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class RelationFormType:
    class Meta:
        name = "relationFormType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
    uri_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriRef",
            "type": "Attribute",
        }
    )
