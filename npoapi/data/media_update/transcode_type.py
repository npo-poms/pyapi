from dataclasses import dataclass, field
from typing import Optional
from ..media.encryption import Encryption
from .priority_type import PriorityType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class TranscodeType:
    class Meta:
        name = "transcodeType"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    encryption: Optional[Encryption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    priority: Optional[PriorityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
