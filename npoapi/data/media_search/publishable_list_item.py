from dataclasses import dataclass, field
from typing import Optional
from ..shared.workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class PublishableListItem:
    class Meta:
        name = "publishableListItem"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    deleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
