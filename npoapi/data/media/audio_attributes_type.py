from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class AudioAttributesType:
    class Meta:
        name = "audioAttributesType"

    numberOfChannels: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    audioCoding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    language: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
