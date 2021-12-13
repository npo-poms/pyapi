from dataclasses import dataclass, field
from typing import Optional
from .media_pager_type_order import MediaPagerTypeOrder
from .media_sort_field import MediaSortField

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class MediaPagerType:
    class Meta:
        name = "mediaPagerType"

    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "min_inclusive": 0,
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
            "min_inclusive": 0,
        }
    )
    sort: Optional[MediaSortField] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    order: Optional[MediaPagerTypeOrder] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
