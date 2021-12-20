from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Names:
    class Meta:
        name = "names"

    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
