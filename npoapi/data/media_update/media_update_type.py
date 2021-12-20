from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from ..media.age_rating_type import AgeRatingType
from ..media.av_type_enum import AvTypeEnum
from ..media.content_rating_type import ContentRatingType
from ..media.intention_enum import IntentionEnum
from ..media.target_group_enum import TargetGroupEnum
from .asset_type import AssetType
from .av_atribute_update_type import AvAtributeUpdateType
from .credits_update_type import CreditsUpdateType
from .description_update_type import DescriptionUpdateType
from .geo_locations_update_type import GeoLocationsUpdateType
from .geo_restriction_update_type import GeoRestrictionUpdateType
from .image_update_type import ImageUpdateType
from .location_update_type import LocationUpdateType
from .member_ref_update_type import MemberRefUpdateType
from .portal_restriction_update_type import PortalRestrictionUpdateType
from .prediction_update_type import PredictionUpdateType
from .relation_update_type import RelationUpdateType
from .schedule_event_update_type import ScheduleEventUpdateType
from .title_update_type import TitleUpdateType
from .topics_update_type import TopicsUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class MediaUpdateType:
    """
    :ivar crid:
    :ivar broadcaster:
    :ivar portal:
    :ivar exclusive:
    :ivar region:
    :ivar title: Titles in dutch
    :ivar description: Descriptions in dutch
    :ivar tag:
    :ivar country: Countries somehow associated with this item. This does not refer to the used language in the
        meta fields of this object. Only supported if version &gt;= 5.0.
    :ivar language: Languages somehow associated with this item. This does not refer to the used language in the
        meta fields of this object. They should be in dutch. Only supported if version &gt;= 5.0.
    :ivar genre:
    :ivar intentions:
    :ivar targetGroups:
    :ivar geoLocations:
    :ivar topics:
    :ivar avAttributes:
    :ivar releaseYear:
    :ivar duration:
    :ivar credits:
    :ivar memberOf:
    :ivar ageRating:
    :ivar contentRating:
    :ivar email:
    :ivar website:
    :ivar twitterref: Only supported if version &gt;= 5.10.
    :ivar prediction: With predictions it can be indicated for which platforms locations will be available. If
        there is a prediction for a certain platform, but the mediaobject is not yet available on the streaming
        platform, then there will be no associated location for that certain platform. If the streaming platform
        status changes, then according to these 'prediction' records the locations will be changed.
    :ivar locations:
    :ivar scheduleEvents: Please note that this is only available for program upates (since 5.11)
    :ivar relation:
    :ivar images:
    :ivar asset:
    :ivar avType:
    :ivar deleted:
    :ivar embeddable:
    :ivar publishStart:
    :ivar publishStop:
    :ivar mid:
    :ivar urn:
    :ivar ordered:
    :ivar version: The POMS version this XML applies too. This is optional, though some feature will only be
        supported if you explicitely specify a version which is big enough (To ensure backward compatiblity).
    """
    class Meta:
        name = "mediaUpdateType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_occurs": 1,
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
    exclusive: List[PortalRestrictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    region: List[GeoRestrictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    title: List[TitleUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_occurs": 1,
        }
    )
    description: List[DescriptionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    country: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"3(\.[0-9]+)+",
        }
    )
    intentions: Optional["MediaUpdateType.Intentions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    targetGroups: Optional["MediaUpdateType.TargetGroups"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    geoLocations: Optional[GeoLocationsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    topics: Optional[TopicsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    avAttributes: Optional[AvAtributeUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    releaseYear: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    credits: Optional[CreditsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    memberOf: List[MemberRefUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    ageRating: Optional[AgeRatingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    contentRating: List[ContentRatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    website: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    twitterref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 2,
            "max_length": 16,
            "pattern": r"[@#][A-Za-z0-9_]{1,139}",
        }
    )
    prediction: List[PredictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    locations: Optional["MediaUpdateType.Locations"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    scheduleEvents: Optional["MediaUpdateType.ScheduleEvents"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    relation: List[RelationUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    images: Optional["MediaUpdateType.Images"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    asset: Optional[AssetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    avType: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    deleted: Optional[bool] = field(
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
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+(\.[0-9]+(\.[0-9]+)?)?",
        }
    )

    @dataclass
    class Intentions:
        intention: List[IntentionEnum] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class TargetGroups:
        targetGroup: List[TargetGroupEnum] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class Locations:
        location: List[LocationUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class ScheduleEvents:
        scheduleEvent: List[ScheduleEventUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class Images:
        image: List[ImageUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )
