from dataclasses import dataclass, field
from typing import List
from .name_update_type import NameUpdateType
from .person_update_type import PersonUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class CreditsUpdateType:
    class Meta:
        name = "creditsUpdateType"

    person_or_name: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "person",
                    "type": PersonUpdateType,
                    "namespace": "urn:vpro:media:update:2009",
                },
                {
                    "name": "name",
                    "type": NameUpdateType,
                    "namespace": "urn:vpro:media:update:2009",
                },
            ),
        }
    )
