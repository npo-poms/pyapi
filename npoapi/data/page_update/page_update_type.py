from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ..page.page_type_enum import PageTypeEnum
from ..page.page_workflow import PageWorkflow
from .embed_update_type import EmbedUpdateType
from .image import Image
from .link_update_type import LinkUpdateType
from .paragraph_update_type import ParagraphUpdateType
from .portal_update_type import PortalUpdateType
from .relation_update_type import RelationUpdateType

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
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
    :ivar type:
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
        }
    )
    alternativeUrl: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
            "min_occurs": 1,
        }
    )
    portal: Optional[PortalUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
            "required": True,
        }
    )
    subtitle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    paragraphs: Optional["PageUpdateType.Paragraphs"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    link: List[LinkUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    embeds: Optional["PageUpdateType.Embeds"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    statRef: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    image: List[Image] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    relation: List[RelationUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:update:2013",
        }
    )
    type: Optional[PageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    lastPublished: Optional[XmlDateTime] = field(
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
    workflow: Optional[PageWorkflow] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Paragraphs:
        paragraph: List[ParagraphUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:update:2013",
            }
        )

    @dataclass
    class Embeds:
        embed: List[EmbedUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:update:2013",
            }
        )
