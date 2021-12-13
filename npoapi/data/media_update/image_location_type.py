from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ImageLocationType:
    """
    :ivar mime_type: Sometimes it may be usefull to explicitely specify the mimetype of the given location. (E.g.
        if there are no or no correct http content type headers).
    :ivar url:
    """
    class Meta:
        name = "imageLocationType"

    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "max_length": 1024,
            "pattern": r"[a-z][a-z]+:.*",
        }
    )
