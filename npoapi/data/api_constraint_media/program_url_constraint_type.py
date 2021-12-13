from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class ProgramUrlConstraintType:
    """
    Constraints on the program url field of locations.
    """
    class Meta:
        name = "programUrlConstraintType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    exact: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
