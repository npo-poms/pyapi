from dataclasses import dataclass, field
from typing import List
from .name_type import NameType
from .person_type import PersonType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class CreditsType:
    class Meta:
        name = "creditsType"

    personOrName: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "person",
                    "type": PersonType,
                    "namespace": "urn:vpro:media:2009",
                },
                {
                    "name": "name",
                    "type": NameType,
                    "namespace": "urn:vpro:media:2009",
                },
            ),
        }
    )
