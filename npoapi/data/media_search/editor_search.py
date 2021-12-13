from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class EditorSearch:
    class Meta:
        name = "editorSearch"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    principal_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "principalId",
            "type": "Attribute",
        }
    )
