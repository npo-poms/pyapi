from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .image_type_enum import ImageTypeEnum
from .license_enum import LicenseEnum
from .owner_type_enum import OwnerTypeEnum
from .workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:shared:2009"


@dataclass
class ImageType:
    class Meta:
        name = "imageType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    imageUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    sourceName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        }
    )
    type: Optional[ImageTypeEnum] = field(
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
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
