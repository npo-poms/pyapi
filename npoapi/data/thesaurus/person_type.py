from dataclasses import dataclass, field
from typing import List, Optional
from .names import Names

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class PersonType:
    class Meta:
        name = "personType"

    name: Optional[str] = field(
        default=None,
        metadata={
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
    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    scope_note: List[str] = field(
        default_factory=list,
        metadata={
            "name": "scopeNote",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    known_as: List[Names] = field(
        default_factory=list,
        metadata={
            "name": "knownAs",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    redirected_from: Optional[str] = field(
        default=None,
        metadata={
            "name": "redirectedFrom",
            "type": "Element",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
            "namespace": "urn:vpro:gtaa:2017",
        }
    )
