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
    :ivar source_name: A simple string representing the source of the image. E.g. 'flickr'.
    :ivar license:
    :ivar width:
    :ivar height:
    :ivar credits:
    :ivar date:
    :ivar offset:
    :ivar image_data: The image as a base-64 encoded blob.
    :ivar image_location: An URL from where the image can be downloaded from.
    :ivar urn: The URN of an already existing image inside the POMS image server.
    :ivar type:
    :ivar urn_attribute:
    :ivar publish_start:
    :ivar publish_stop:
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
    source_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceName",
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
    image_data: Optional[ImageDataType] = field(
        default=None,
        metadata={
            "name": "imageData",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    image_location: Optional[ImageLocationType] = field(
        default=None,
        metadata={
            "name": "imageLocation",
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
    urn_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "urn",
            "type": "Attribute",
        }
    )
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
