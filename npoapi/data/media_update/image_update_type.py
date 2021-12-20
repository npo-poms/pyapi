from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .image_data_type import ImageDataType
from .image_location_type import ImageLocationType
from ..shared.image_type_enum import ImageTypeEnum
from ..shared.license_enum import LicenseEnum

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ImageUpdateType:
    """
    :ivar title:
    :ivar description:
    :ivar source: The source of the image. This is only metadata. It must be URL from where the image was
        originally acquired.
    :ivar sourceName: A simple string representing the source of the image. E.g. 'flickr'.
    :ivar license:
    :ivar width:
    :ivar height:
    :ivar credits:
    :ivar date:
    :ivar offset:
    :ivar imageData: The image as a base-64 encoded blob.
    :ivar imageLocation: An URL from where the image can be downloaded from.
    :ivar urn: The URN of an already existing image inside the POMS image server.
    :ivar type:
    :ivar urnAttribute:
    :ivar publishStart:
    :ivar publishStop:
    :ivar highlighted:
    """
    class Meta:
        name = "imageUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    sourceName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    imageData: Optional[ImageDataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    imageLocation: Optional[ImageLocationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"urn:vpro[\.:]image:[0-9]+",
        }
    )
    type: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    urnAttribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "urn",
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
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
