from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Names:
    class Meta:
        name = "names"

    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
