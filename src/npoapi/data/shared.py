from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration

__NAMESPACE__ = "urn:vpro:shared:2009"


class ImageTypeEnum(Enum):
    PICTURE = "PICTURE"
    PORTRAIT = "PORTRAIT"
    STILL = "STILL"
    LOGO = "LOGO"
    ICON = "ICON"
    PROMO_LANDSCAPE = "PROMO_LANDSCAPE"
    PROMO_PORTRAIT = "PROMO_PORTRAIT"
    BACKGROUND = "BACKGROUND"


class LicenseEnum(Enum):
    COPYRIGHTED = "COPYRIGHTED"
    PUBLIC_DOMAIN = "PUBLIC_DOMAIN"
    CC_BY = "CC_BY"
    CC_BY_SA = "CC_BY_SA"
    CC_BY_ND = "CC_BY_ND"
    CC_BY_NC = "CC_BY_NC"
    CC_BY_NC_SA = "CC_BY_NC_SA"
    CC_BY_NC_ND = "CC_BY_NC_ND"
    USA_GOV = "USA_GOV"
    CC_MARK = "CC_MARK"


class OwnerTypeEnum(Enum):
    BROADCASTER = "BROADCASTER"
    NEBO = "NEBO"
    NPO = "NPO"
    MIS = "MIS"
    CERES = "CERES"
    PLUTO = "PLUTO"
    PROJECTM = "PROJECTM"
    WHATS_ON = "WHATS_ON"
    IMMIX = "IMMIX"
    AUTHORITY = "AUTHORITY"
    RADIOBOX = "RADIOBOX"
    BEELDENGELUID = "BEELDENGELUID"
    TEMPORARY = "TEMPORARY"


class SubtitlesTypeEnum(Enum):
    """The type of a subtitles object.

    TODO these descriptions are provisional?

    :cvar CAPTION: The subtitles represent a textual version of what is spoken or wat is happening. They are
        expected to be in the same language as the video itself. Teletekst 888 subtitles are captions.
    :cvar TRANSLATION: The subtitles represent a translation. They are expected to be in a different language
        than the main language that can be heard
    :cvar TRANSCRIPT: The subtitles represent a precise or automatic version of what is being said.
    """

    CAPTION = "CAPTION"
    TRANSLATION = "TRANSLATION"
    TRANSCRIPT = "TRANSCRIPT"


class SubtitlesWorkflowEnum(Enum):
    IGNORE = "IGNORE"
    REVOKED = "REVOKED"
    DELETED = "DELETED"
    FOR_DELETION = "FOR_DELETION"
    PUBLISHED = "PUBLISHED"
    FOR_PUBLICATION = "FOR_PUBLICATION"
    FOR_REPUBLICATION = "FOR_REPUBLICATION"
    PUBLISH_ERROR = "PUBLISH_ERROR"
    MISSING = "MISSING"


class WorkflowEnumType(Enum):
    """These are the possible values of several 'workflow' fields.

    These serve administrative purposes only. In the Frontent API you should only encounter 'PUBLISHED'.

    :cvar FOR_PUBLICATION:
    :cvar FOR_REPUBLICATION:
    :cvar PUBLISHED:
    :cvar PARENT_REVOKED:
    :cvar REVOKED:
    :cvar FOR_DELETION:
    :cvar DELETED:
    :cvar MERGED:
    :cvar IGNORE: This means that the object is ignored for workflow changes. This is mainly usefull during
        testing.
    :cvar TEMPORARY:
    """

    FOR_PUBLICATION = "FOR PUBLICATION"
    FOR_REPUBLICATION = "FOR REPUBLICATION"
    PUBLISHED = "PUBLISHED"
    PARENT_REVOKED = "PARENT REVOKED"
    REVOKED = "REVOKED"
    FOR_DELETION = "FOR DELETION"
    DELETED = "DELETED"
    MERGED = "MERGED"
    IGNORE = "IGNORE"
    TEMPORARY = "TEMPORARY"


@dataclass(slots=True)
class ImageType:
    """
    :ivar title:
    :ivar description:
    :ivar imageUri:
    :ivar offset:
    :ivar height:
    :ivar width:
    :ivar credits:
    :ivar source: Where this image was found. In words. E.g. 'ANP'
    :ivar sourceName: Where this image was found. As an URL.
    :ivar license:
    :ivar crid:
    :ivar date:
    :ivar typeValue:
    :ivar owner:
    :ivar highlighted:
    :ivar urn:
    :ivar publishStart:
    :ivar publishStop:
    :ivar publishDate:
    :ivar creationDate:
    :ivar lastModified:
    :ivar workflow:
    """

    class Meta:
        name = "imageType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
            "required": True,
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    imageUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    sourceName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:shared:2009",
        },
    )
    typeValue: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    creationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class PublishableObjectType:
    class Meta:
        name = "publishableObjectType"

    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    creationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Image(ImageType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:shared:2009"
