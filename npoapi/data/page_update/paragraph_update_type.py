from dataclasses import dataclass, field
from typing import Optional
from .image import Image

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class ParagraphUpdateType:
    class Meta:
        name = "paragraphUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    image: Optional[Image] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
