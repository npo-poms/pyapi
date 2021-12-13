from dataclasses import dataclass
from .image_update_type import ImageUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Image(ImageUpdateType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:media:update:2009"
