from dataclasses import dataclass
from .publishable_list_item import PublishableListItem

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class ImageListItem(PublishableListItem):
    class Meta:
        name = "imageListItem"
