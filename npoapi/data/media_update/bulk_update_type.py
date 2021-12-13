from dataclasses import dataclass, field
from typing import Optional
from .description_update_type import DescriptionUpdateType
from .title_update_type import TitleUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class BulkUpdateType:
    class Meta:
        name = "bulkUpdateType"

    titles: Optional[TitleUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    descriptions: Optional[DescriptionUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
