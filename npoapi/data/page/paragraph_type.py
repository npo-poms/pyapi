from dataclasses import dataclass, field
from typing import Optional
from .image_type import ImageType

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class ParagraphType:
    class Meta:
        name = "paragraphType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    image: Optional[ImageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
