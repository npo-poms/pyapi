from dataclasses import dataclass, field
from typing import List
from ..shared.image import Image

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ImagesType:
    class Meta:
        name = "imagesType"

    image: List[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
