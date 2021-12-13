from dataclasses import dataclass
from .itemize_response_type import ItemizeResponseType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ItemizeResponse(ItemizeResponseType):
    class Meta:
        name = "itemizeResponse"
        namespace = "urn:vpro:media:update:2009"
