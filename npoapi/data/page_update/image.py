from dataclasses import dataclass
from .image_update_type import ImageUpdateType

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class Image(ImageUpdateType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:pages:update:2013"
