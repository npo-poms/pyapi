from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ..media.broadcaster_type import BroadcasterType
from .embed_type import EmbedType
from .genre import Genre
from .image_type import ImageType
from .link_type import LinkType
from .page_type_enum import PageTypeEnum
from .page_workflow import PageWorkflow
from .paragraph_type import ParagraphType
from .portal_type import PortalType
from .referral_type import ReferralType
from .relation_type import RelationType

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class PageType:
    class Meta:
        name = "pageType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    alternativeUrl: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    broadcaster: List[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "min_occurs": 1,
        }
    )
    portal: Optional[PortalType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
            "required": True,
        }
    )
    subTitle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    keyword: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    genre: List[Genre] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    summary: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    paragraphs: Optional["PageType.Paragraphs"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    referral: List[ReferralType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    link: List[LinkType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    embed: List[EmbedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    statRef: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    images: Optional["PageType.Images"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    relation: List[RelationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[PageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
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
    lastPublished: Optional[XmlDateTime] = field(
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
    refCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sortDate: Optional[XmlDateTime] = field(
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
        paragraph: List[ParagraphType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            }
        )

    @dataclass
    class Images:
        image: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:pages:2013",
            }
        )
