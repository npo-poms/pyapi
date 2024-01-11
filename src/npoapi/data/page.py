from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDateTime
from npoapi.data.media import (
    BroadcasterType,
    Group,
    Program,
    Segment,
)
from npoapi.data.shared import (
    ImageTypeEnum,
    LicenseEnum,
)

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass(slots=True)
class GenreType:
    class Meta:
        name = "genreType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    displayName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class LinkTypeEnum(Enum):
    TOP_STORY = "TOP_STORY"


class PageTypeEnum(Enum):
    ARTICLE = "ARTICLE"
    SPECIAL = "SPECIAL"
    HOME = "HOME"
    OVERVIEW = "OVERVIEW"
    PRODUCT = "PRODUCT"
    PLAYER = "PLAYER"
    AUDIO = "AUDIO"
    VIDEO = "VIDEO"
    MIXED = "MIXED"
    PLAYLIST = "PLAYLIST"
    MOVIE = "MOVIE"
    SERIES = "SERIES"
    PERSON = "PERSON"
    SEARCH = "SEARCH"


class PageWorkflow(Enum):
    PUBLISHED = "PUBLISHED"
    DELETED = "DELETED"


@dataclass(slots=True)
class RelationType:
    class Meta:
        name = "relationType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    uriRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


@dataclass(slots=True)
class SectionType:
    class Meta:
        name = "sectionType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    path: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class EmbedType:
    class Meta:
        name = "embedType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    groupOrProgramOrSegment: Optional[Union[Group, Program, Segment]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "group",
                    "type": Group,
                    "namespace": "urn:vpro:media:2009",
                },
                {
                    "name": "program",
                    "type": Program,
                    "namespace": "urn:vpro:media:2009",
                },
                {
                    "name": "segment",
                    "type": Segment,
                    "namespace": "urn:vpro:media:2009",
                },
            ),
        },
    )


@dataclass(slots=True)
class Genre(GenreType):
    class Meta:
        name = "genre"
        namespace = "urn:vpro:pages:2013"


@dataclass(slots=True)
class ImageType:
    class Meta:
        name = "imageType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    sourceName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    typeValue: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class LinkType:
    class Meta:
        name = "linkType"

    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
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
class PortalType:
    class Meta:
        name = "portalType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "required": True,
        },
    )
    section: Optional[SectionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
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
class ReferralType:
    class Meta:
        name = "referralType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    referrer: Optional[str] = field(
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
class ParagraphType:
    class Meta:
        name = "paragraphType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    body: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    image: Optional[ImageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )


@dataclass(slots=True)
class PageType:
    class Meta:
        name = "pageType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    alternativeUrl: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    broadcaster: List[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "min_occurs": 1,
        },
    )
    portal: Optional[PortalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "required": True,
        },
    )
    subTitle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    genre: List[Genre] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    paragraphs: Optional["PageType.Paragraphs"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    referral: List[ReferralType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    embed: List[EmbedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    statRef: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    images: Optional["PageType.Images"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    relation: List[RelationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
    lastPublished: Optional[XmlDateTime] = field(
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
    refCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sortDate: Optional[XmlDateTime] = field(
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
    class Paragraphs:
        paragraph: List[ParagraphType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            },
        )

    @dataclass(slots=True)
    class Images:
        image: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            },
        )


@dataclass(slots=True)
class Page(PageType):
    class Meta:
        name = "page"
        namespace = "urn:vpro:pages:2013"
