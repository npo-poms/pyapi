from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .age_rating_type import AgeRatingType
from .av_attributes_type import AvAttributesType
from .av_type_enum import AvTypeEnum
from .available_subtitle_type import AvailableSubtitleType
from .broadcaster_type import BroadcasterType
from .content_rating_type import ContentRatingType
from .country_type import CountryType
from .credits_type import CreditsType
from .descendant_ref_type import DescendantRefType
from .description_type import DescriptionType
from .genre_type import GenreType
from .geo_locations_type import GeoLocationsType
from .geo_restriction_type import GeoRestrictionType
from .images_type import ImagesType
from .intention_type import IntentionType
from .language_type import LanguageType
from .locations_type import LocationsType
from .member_ref_type import MemberRefType
from .organization_type import OrganizationType
from .portal_restriction_type import PortalRestrictionType
from .prediction_type import PredictionType
from .relation_type import RelationType
from .tag_type import TagType
from .target_groups_type import TargetGroupsType
from .title_type import TitleType
from .topics_type import TopicsType
from .twitter_type import TwitterType
from ..shared.workflow_enum_type import WorkflowEnumType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class BaseMediaType:
    """This is the abstract base entity for programs, groups and segments.

    Actually these objects are very similar and share most properties.

    :ivar crid: A crid (content reference identifier) is a reference to an entity in another system. E.g. a crid
        like crid://broadcast.radiobox2/335793 refers to a broadcast with id 335793 in Radiobox. A crid must be a
        valid URI starting with "crid://". Crids must be unique, but they can be made up freely. It is a good
        idea to use a logical structure which can easily be associated with another system. Any POMS object can
        have zero or more crids. They can refer to different systems, but a POMS object could also actually
        represent more than one entity in a remote system.
    :ivar broadcaster: One or more broadcasters can be the owner of a POMS media object. This information is meta
        information about the object, but it is also used for assigning write access to the object in the POMS
        backend to employees of these given broadcasting companies.
    :ivar portal: Optionally 'portals' can be assigned to a media object. Portals are also 'owners', and
        employees can also work for a certain portal. This is because some portal are shared by several
        broadcasting companies.
    :ivar exclusive: Besides having portals, which mainly indicates where the object originates, a media object
        can also be assigned 'portal restrictions'. If a media object has any portal restrictions the media
        object may only be shown on these portals.
    :ivar region: Media with a geo restriction can only be played in the indicated region (NL, BENELUX, WORLD).
        This restriction doesn't apply to the metadata of the media object. It only applies to the actual
        playable content.
    :ivar title: A media object has one or more titles. All titles have a type (MAIN, SUB etc.) and an owner
        (BROADCASTER, MIS etc.). The combination of type and owner is always unique for a particular media
        object, so a media object cannot have multiple titles of the same type and owner. Titles are sorted in
        order of the textualTypeEnum and the in order of ownerTypeEnum when published, so the first title in a
        published document will be a title owned by BROADCASTER of type MAIN, if that title exists.
    :ivar description: Optional descriptions for the media object. Descriptions have an owner and a type, and are
        ordered just like titles.
    :ivar genre:
    :ivar tag:
    :ivar intentions:
    :ivar targetGroups:
    :ivar geoLocations:
    :ivar topics:
    :ivar source:
    :ivar country:
    :ivar language:
    :ivar isDubbed:
    :ivar availableSubtitles:
    :ivar avAttributes:
    :ivar releaseYear:
    :ivar duration:
    :ivar credits:
    :ivar award:
    :ivar descendantOf:
    :ivar memberOf:
    :ivar ageRating:
    :ivar contentRating:
    :ivar email:
    :ivar website:
    :ivar twitter:
    :ivar teletext:
    :ivar prediction:
    :ivar locations:
    :ivar relation:
    :ivar images:
    :ivar mid:
    :ivar avType:
    :ivar sortDate:
    :ivar embeddable:
    :ivar hasSubtitles:
    :ivar urn:
    :ivar publishStart:
    :ivar publishStop:
    :ivar publishDate:
    :ivar creationDate:
    :ivar lastModified:
    :ivar workflow:
    :ivar mergedTo:
    """
    class Meta:
        name = "baseMediaType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    broadcaster: List[BroadcasterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )
    portal: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    exclusive: List[PortalRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    region: List[GeoRestrictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    title: List[TitleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_occurs": 1,
        }
    )
    description: List[DescriptionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    genre: List[GenreType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    tag: List[TagType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    intentions: List[IntentionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    targetGroups: List[TargetGroupsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    geoLocations: List[GeoLocationsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    topics: List[TopicsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    country: List[CountryType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    language: List[LanguageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    isDubbed: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    availableSubtitles: List[AvailableSubtitleType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    avAttributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    releaseYear: Optional[int] = field(
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
    credits: Optional[CreditsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    award: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    descendantOf: List[DescendantRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    memberOf: List[MemberRefType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    ageRating: Optional[AgeRatingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    contentRating: List[ContentRatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    website: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    twitter: List[TwitterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    teletext: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    prediction: List[PredictionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    locations: Optional[LocationsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    relation: List[RelationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    images: Optional[ImagesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    avType: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    sortDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    embeddable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    hasSubtitles: bool = field(
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
    mergedTo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
