from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class TagType:
    class Meta:
        name = "tagType"

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
