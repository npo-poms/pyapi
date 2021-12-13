from dataclasses import dataclass, field
from typing import List, Optional
from .itemize_type import ItemizeType
from .live_itemize_1 import LiveItemize1

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ItemizeResponseType:
    class Meta:
        name = "itemizeResponseType"

    request: Optional[ItemizeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    liverequest: Optional[LiveItemize1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    result: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
