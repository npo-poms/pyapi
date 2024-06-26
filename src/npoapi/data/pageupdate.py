from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime, XmlDuration

from npoapi.data.page import (
    LinkTypeEnum,
    PageIdMatch,
    PageTypeEnum,
    PageWorkflow,
    SectionType,
)
from npoapi.data.shared import (
    ImageTypeEnum,
    LicenseEnum,
)

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass(slots=True)
class EmbedUpdateType:
    class Meta:
        name = "embedUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    midRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class ImageLocationType:
    class Meta:
        name = "imageLocationType"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )


@dataclass(slots=True)
class RelationUpdateType:
    class Meta:
        name = "relationUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    typeValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    uriRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class SaveResult:
    class Meta:
        name = "saveResult"
        namespace = "urn:vpro:pages:update:2013"

    replaces: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    creationDate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class DeleteResult:
    class Meta:
        name = "deleteResult"
        namespace = "urn:vpro:pages:update:2013"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    notallowedCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    alreadyDeletedCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    match: Optional[PageIdMatch] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class ImageUpdateType:
    class Meta:
        name = "imageUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    sourceName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    imageLocation: Optional[ImageLocationType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    typeValue: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class LinkUpdateType:
    class Meta:
        name = "linkUpdateType"

    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    pageRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    typeValue: Optional[LinkTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class PageUpdateTypeEmbeds:
    class Meta:
        global_type = False

    embed: List[EmbedUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )


@dataclass(slots=True)
class PortalUpdateType:
    class Meta:
        name = "portalUpdateType"

    section: Optional[SectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class SaveResultList:
    class Meta:
        name = "saveResultList"

    saveResult: List[SaveResult] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )


@dataclass(slots=True)
class Image(ImageUpdateType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:pages:update:2013"


@dataclass(slots=True)
class SaveResults(SaveResultList):
    class Meta:
        name = "saveResults"
        namespace = "urn:vpro:pages:update:2013"


@dataclass(slots=True)
class ParagraphUpdateType:
    class Meta:
        name = "paragraphUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    image: Optional[Image] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )


@dataclass(slots=True)
class PageUpdateTypeParagraphs:
    class Meta:
        global_type = False

    paragraph: List[ParagraphUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )


@dataclass(slots=True)
class PageUpdateType:
    """
    :ivar crid:
    :ivar alternativeUrl:
    :ivar broadcaster:
    :ivar portal:
    :ivar title:
    :ivar subtitle:
    :ivar keyword:
    :ivar summary:
    :ivar paragraphs:
    :ivar tag:
    :ivar genre: Genres, as specified in https://publish.pages.omroep.nl/schema/classification
    :ivar link:
    :ivar embeds:
    :ivar statRef:
    :ivar image:
    :ivar relation:
    :ivar typeValue:
    :ivar url:
    :ivar publishStart:
    :ivar lastPublished:
    :ivar creationDate:
    :ivar lastModified:
    :ivar workflow:
    """

    class Meta:
        name = "pageUpdateType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    alternativeUrl: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
            "min_occurs": 1,
        },
    )
    portal: Optional[PortalUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
            "required": True,
        },
    )
    subtitle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    paragraphs: Optional[PageUpdateTypeParagraphs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    link: List[LinkUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    embeds: Optional[PageUpdateTypeEmbeds] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    statRef: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    image: List[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    relation: List[RelationUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        },
    )
    typeValue: Optional[PageTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lastPublished: Optional[XmlDateTime] = field(
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
    workflow: Optional[PageWorkflow] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Page(PageUpdateType):
    class Meta:
        name = "page"
        namespace = "urn:vpro:pages:update:2013"
