from dataclasses import dataclass, field
from typing import List, Optional
from .media_list_item import MediaListItem
from .media_list_result_type_order import MediaListResultTypeOrder

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class MediaListResultType:
    class Meta:
        name = "mediaListResultType"

    item: List[MediaListItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    total_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalCount",
            "type": "Attribute",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sort: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    order: Optional[MediaListResultTypeOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
