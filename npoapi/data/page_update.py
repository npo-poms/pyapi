from dataclasses import dataclass, field
from typing import List, Optional
from npoapi.data.page import (
    LinkTypeEnum,
    PageTypeEnum,
    PageWorkflow,
    SectionType,
)
from npoapi.data.shared import (
    ImageTypeEnum,
    LicenseEnum,
)

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class EmbedUpdateType:
    """
    :ivar title:
    :ivar description:
    :ivar mid_ref:
    """
    class Meta:
        name = "embedUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="midRef",
            type="Attribute"
        )
    )


@dataclass
class ImageLocationType:
    """
    :ivar url:
    """
    class Meta:
        name = "imageLocationType"

    url: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )


@dataclass
class RelationUpdateType:
    """
    :ivar value:
    :ivar type:
    :ivar broadcaster:
    :ivar uri_ref:
    """
    class Meta:
        name = "relationUpdateType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    uri_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="uriRef",
            type="Attribute"
        )
    )


@dataclass
class ImageUpdateType:
    """
    :ivar title:
    :ivar description:
    :ivar source:
    :ivar source_name:
    :ivar license:
    :ivar credits:
    :ivar image_location:
    :ivar type:
    """
    class Meta:
        name = "imageUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    description: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    source: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    source_name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="sourceName",
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    credits: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    image_location: Optional[ImageLocationType] = field(
        default=None,
        metadata=dict(
            name="imageLocation",
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    type: Optional[ImageTypeEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class LinkUpdateType:
    """
    :ivar text:
    :ivar page_ref:
    :ivar type:
    """
    class Meta:
        name = "linkUpdateType"

    text: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    page_ref: Optional[str] = field(
        default=None,
        metadata=dict(
            name="pageRef",
            type="Attribute"
        )
    )
    type: Optional[LinkTypeEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class PortalUpdateType:
    """
    :ivar section:
    :ivar id:
    :ivar url:
    """
    class Meta:
        name = "portalUpdateType"

    section: Optional[SectionType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    id: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    url: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )


@dataclass
class Image(ImageUpdateType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:pages:update:2013"


@dataclass
class ParagraphUpdateType:
    """
    :ivar title:
    :ivar body:
    :ivar image:
    """
    class Meta:
        name = "paragraphUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    body: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    image: Optional[Image] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )


@dataclass
class PageUpdateType:
    """
    :ivar crid:
    :ivar alternative_url:
    :ivar broadcaster:
    :ivar portal:
    :ivar title:
    :ivar subtitle:
    :ivar keyword:
    :ivar summary:
    :ivar paragraphs:
    :ivar tag:
    :ivar genre:
    :ivar link:
    :ivar embeds:
    :ivar stat_ref:
    :ivar image:
    :ivar relation:
    :ivar type:
    :ivar url:
    :ivar publish_start:
    :ivar last_published:
    :ivar creation_date:
    :ivar last_modified:
    :ivar workflow:
    """
    class Meta:
        name = "pageUpdateType"

    crid: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    alternative_url: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="alternativeUrl",
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    portal: Optional[PortalUpdateType] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    title: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            required=True
        )
    )
    subtitle: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    summary: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    paragraphs: Optional["PageUpdateType.Paragraphs"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    tag: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    genre: List[str] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    link: List[LinkUpdateType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    embeds: Optional["PageUpdateType.Embeds"] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013"
        )
    )
    stat_ref: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="statRef",
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    image: List[Image] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    relation: List[RelationUpdateType] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:pages:update:2013",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    type: Optional[PageTypeEnum] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    url: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True
        )
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata=dict(
            name="publishStart",
            type="Attribute"
        )
    )
    last_published: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lastPublished",
            type="Attribute"
        )
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata=dict(
            name="creationDate",
            type="Attribute"
        )
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata=dict(
            name="lastModified",
            type="Attribute"
        )
    )
    workflow: Optional[PageWorkflow] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )

    @dataclass
    class Paragraphs:
        """
        :ivar paragraph:
        """
        paragraph: List[ParagraphUpdateType] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                namespace="urn:vpro:pages:update:2013",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )

    @dataclass
    class Embeds:
        """
        :ivar embed:
        """
        embed: List[EmbedUpdateType] = field(
            default_factory=list,
            metadata=dict(
                type="Element",
                namespace="urn:vpro:pages:update:2013",
                min_occurs=0,
                max_occurs=9223372036854775807
            )
        )


@dataclass
class Page(PageUpdateType):
    class Meta:
        name = "page"
        namespace = "urn:vpro:pages:update:2013"
