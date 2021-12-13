from dataclasses import dataclass, field
from typing import List
from .program import Program

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ProgramTableType:
    class Meta:
        name = "programTableType"

    program: List[Program] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
