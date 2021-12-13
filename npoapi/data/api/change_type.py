from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ..media.base_media_type import BaseMediaType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class ChangeType:
    class Meta:
        name = "changeType"

    media: Optional[BaseMediaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    publish_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishDate",
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    deleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tail: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    revision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    merged_to: Optional[str] = field(
        default=None,
        metadata={
            "name": "mergedTo",
            "type": "Attribute",
        }
    )
    real_publish_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "realPublishDate",
            "type": "Attribute",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
