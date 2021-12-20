from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .av_attributes_type import AvAttributesType
from .location_type_enum import LocationTypeEnum
from .platform_type_enum import PlatformTypeEnum
from ..shared.owner_type_enum import OwnerTypeEnum
from ..shared.workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class LocationType:
    class Meta:
        name = "locationType"

    programUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    avAttributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    subtitles: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    type: Optional[LocationTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    publishDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    creationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
