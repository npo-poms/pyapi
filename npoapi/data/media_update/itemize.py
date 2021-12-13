from dataclasses import dataclass
from .itemize_type import ItemizeType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Itemize(ItemizeType):
    class Meta:
        name = "itemize"
        namespace = "urn:vpro:media:update:2009"
