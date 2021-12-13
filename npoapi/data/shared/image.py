from dataclasses import dataclass
from .image_type import ImageType

__NAMESPACE__ = "urn:vpro:shared:2009"


@dataclass
class Image(ImageType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:shared:2009"
