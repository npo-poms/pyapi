from dataclasses import dataclass, field
from typing import Optional
from ..media.group import Group
from ..media.program import Program
from ..media.segment import Segment

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class EmbedType:
    class Meta:
        name = "embedType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment: Optional[Segment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
