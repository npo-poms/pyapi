from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:api:constraint:2014"


@dataclass
class LocalizedString:
    class Meta:
        name = "localizedString"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
