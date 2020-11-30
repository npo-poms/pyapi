from dataclasses import dataclass, field
from typing import List, Optional
from npoapi.data.api_constraint import OperatorType
from npoapi.data.media import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class HasAgeRatingConstraintType:
    class Meta:
        name = "hasAgeRatingConstraintType"


@dataclass
class HasContentRatingConstraintType:
    class Meta:
        name = "hasContentRatingConstraintType"


@dataclass
class HasGeoRestrictionConstraintType:
    class Meta:
        name = "hasGeoRestrictionConstraintType"


@dataclass
class HasImageConstraintType:
    class Meta:
        name = "hasImageConstraintType"


@dataclass
class HasLocationConstraintType:
    """
    :ivar platform:
    """
    class Meta:
        name = "hasLocationConstraintType"

    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HasPortalConstraintType:
    class Meta:
        name = "hasPortalConstraintType"


@dataclass
class HasPortalRestrictionConstraintType:
    class Meta:
        name = "hasPortalRestrictionConstraintType"


@dataclass
class ProgramUrlConstraintType:
    """Constraints on the program url field of locations.

    :ivar value:
    :ivar exact:
    """
    class Meta:
        name = "programUrlConstraintType"

    value: Optional[str] = field(
        default=None,
    )
    exact: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeoRestrictionConstraintType:
    """
    :ivar value:
    :ivar platform:
    """
    class Meta:
        name = "geoRestrictionConstraintType"

    value: Optional[str] = field(
        default=None,
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HasPredictionConstraintType:
    """
    :ivar platform:
    """
    class Meta:
        name = "hasPredictionConstraintType"

    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ScheduleEventType:
    """documentation for schedule event date.

    :ivar date: A timestamp spec. This is parsed by the natty parser. Try out with http://natty.joestelmach.com/try.jsp
    :ivar operator:
    """
    class Meta:
        name = "scheduleEventType"

    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    operator: Optional[OperatorType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NotType:
    """
    :ivar and_value:
    :ivar or_value:
    :ivar not_value:
    :ivar av_type:
    :ivar av_file_format:
    :ivar av_file_extension:
    :ivar program_url:
    :ivar descendant_of:
    :ivar broadcaster:
    :ivar has_image:
    :ivar has_location:
    :ivar has_prediction:
    :ivar type:
    :ivar channel:
    :ivar schedule_event:
    :ivar has_portal:
    :ivar portal:
    :ivar is_exclusive:
    :ivar exclusive:
    :ivar has_geo_restriction:
    :ivar geo_restriction:
    :ivar age_rating:
    :ivar has_age_rating:
    :ivar content_rating:
    :ivar has_content_rating:
    :ivar genre:
    """
    class Meta:
        name = "not"

    and_value: Optional["AndType"] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    or_value: Optional["OrType"] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    not_value: Optional["NotType"] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    av_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "avType",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    av_file_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    av_file_extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "avFileExtension",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    program_url: Optional[ProgramUrlConstraintType] = field(
        default=None,
        metadata={
            "name": "programUrl",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    descendant_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    has_image: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasImage",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    has_location: Optional[HasLocationConstraintType] = field(
        default=None,
        metadata={
            "name": "hasLocation",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    has_prediction: Optional[HasPredictionConstraintType] = field(
        default=None,
        metadata={
            "name": "hasPrediction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    channel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    schedule_event: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    has_portal: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasPortal",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    portal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    is_exclusive: Optional[str] = field(
        default=None,
        metadata={
            "name": "isExclusive",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    exclusive: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    has_geo_restriction: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasGeoRestriction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    geo_restriction: Optional[GeoRestrictionConstraintType] = field(
        default=None,
        metadata={
            "name": "geoRestriction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    age_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "ageRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    has_age_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasAgeRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    content_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    has_content_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasContentRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    genre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )


@dataclass
class OrType:
    """
    :ivar and_value:
    :ivar or_value:
    :ivar not_value:
    :ivar av_type:
    :ivar av_file_format:
    :ivar av_file_extension:
    :ivar program_url:
    :ivar descendant_of:
    :ivar broadcaster:
    :ivar has_image:
    :ivar has_location:
    :ivar has_prediction:
    :ivar type:
    :ivar channel:
    :ivar schedule_event:
    :ivar has_portal:
    :ivar portal:
    :ivar is_exclusive:
    :ivar exclusive:
    :ivar has_geo_restriction:
    :ivar geo_restriction:
    :ivar age_rating:
    :ivar has_age_rating:
    :ivar content_rating:
    :ivar has_content_rating:
    :ivar genre:
    """
    class Meta:
        name = "or"

    and_value: List["AndType"] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    or_value: List["OrType"] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    not_value: List[NotType] = field(
        default_factory=list,
        metadata={
            "name": "not",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    av_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "avType",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    av_file_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    av_file_extension: List[str] = field(
        default_factory=list,
        metadata={
            "name": "avFileExtension",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    program_url: List[ProgramUrlConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "programUrl",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    descendant_of: List[str] = field(
        default_factory=list,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_image: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasImage",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_location: List[HasLocationConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "hasLocation",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_prediction: List[HasPredictionConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "hasPrediction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    type: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    channel: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    schedule_event: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_portal: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasPortal",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    is_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "isExclusive",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_geo_restriction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasGeoRestriction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    geo_restriction: List[GeoRestrictionConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "geoRestriction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    age_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ageRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_age_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasAgeRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    content_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "contentRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_content_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasContentRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )


@dataclass
class AndType:
    """
    :ivar and_value:
    :ivar or_value:
    :ivar not_value:
    :ivar av_type:
    :ivar av_file_format:
    :ivar av_file_extension:
    :ivar program_url:
    :ivar descendant_of:
    :ivar broadcaster:
    :ivar has_image:
    :ivar has_location:
    :ivar has_prediction:
    :ivar type:
    :ivar channel:
    :ivar schedule_event:
    :ivar has_portal:
    :ivar portal:
    :ivar is_exclusive:
    :ivar exclusive:
    :ivar has_geo_restriction:
    :ivar geo_restriction:
    :ivar age_rating:
    :ivar has_age_rating:
    :ivar content_rating:
    :ivar has_content_rating:
    :ivar genre:
    """
    class Meta:
        name = "and"

    and_value: List["AndType"] = field(
        default_factory=list,
        metadata={
            "name": "and",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    or_value: List[OrType] = field(
        default_factory=list,
        metadata={
            "name": "or",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    not_value: List[NotType] = field(
        default_factory=list,
        metadata={
            "name": "not",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    av_type: List[str] = field(
        default_factory=list,
        metadata={
            "name": "avType",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    av_file_format: List[str] = field(
        default_factory=list,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    av_file_extension: List[str] = field(
        default_factory=list,
        metadata={
            "name": "avFileExtension",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    program_url: List[ProgramUrlConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "programUrl",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    descendant_of: List[str] = field(
        default_factory=list,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_image: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasImage",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_location: List[HasLocationConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "hasLocation",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_prediction: List[HasPredictionConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "hasPrediction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    type: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    channel: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    schedule_event: List[ScheduleEventType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_portal: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasPortal",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    is_exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "name": "isExclusive",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    exclusive: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_geo_restriction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasGeoRestriction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    geo_restriction: List[GeoRestrictionConstraintType] = field(
        default_factory=list,
        metadata={
            "name": "geoRestriction",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    age_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ageRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_age_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasAgeRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    content_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "contentRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    has_content_rating: List[str] = field(
        default_factory=list,
        metadata={
            "name": "hasContentRating",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
            "sequential": True,
        }
    )


@dataclass
class Filter:
    """
    :ivar and_value:
    :ivar or_value:
    :ivar not_value:
    :ivar av_type:
    :ivar av_file_format:
    :ivar av_file_extension:
    :ivar program_url:
    :ivar descendant_of:
    :ivar broadcaster:
    :ivar has_image:
    :ivar has_location:
    :ivar has_prediction:
    :ivar type:
    :ivar channel:
    :ivar schedule_event:
    :ivar has_portal:
    :ivar portal:
    :ivar is_exclusive:
    :ivar exclusive:
    :ivar has_geo_restriction:
    :ivar geo_restriction:
    :ivar age_rating:
    :ivar has_age_rating:
    :ivar content_rating:
    :ivar has_content_rating:
    :ivar genre:
    """
    class Meta:
        name = "filter"
        namespace = "urn:vpro:api:constraint:media:2013"

    and_value: Optional[AndType] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        }
    )
    or_value: Optional[OrType] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        }
    )
    not_value: Optional[NotType] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        }
    )
    av_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "avType",
            "type": "Element",
        }
    )
    av_file_format: Optional[str] = field(
        default=None,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
        }
    )
    av_file_extension: Optional[str] = field(
        default=None,
        metadata={
            "name": "avFileExtension",
            "type": "Element",
        }
    )
    program_url: Optional[ProgramUrlConstraintType] = field(
        default=None,
        metadata={
            "name": "programUrl",
            "type": "Element",
        }
    )
    descendant_of: Optional[str] = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    has_image: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasImage",
            "type": "Element",
        }
    )
    has_location: Optional[HasLocationConstraintType] = field(
        default=None,
        metadata={
            "name": "hasLocation",
            "type": "Element",
        }
    )
    has_prediction: Optional[HasPredictionConstraintType] = field(
        default=None,
        metadata={
            "name": "hasPrediction",
            "type": "Element",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    channel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    schedule_event: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "name": "scheduleEvent",
            "type": "Element",
        }
    )
    has_portal: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasPortal",
            "type": "Element",
        }
    )
    portal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    is_exclusive: Optional[str] = field(
        default=None,
        metadata={
            "name": "isExclusive",
            "type": "Element",
        }
    )
    exclusive: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    has_geo_restriction: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasGeoRestriction",
            "type": "Element",
        }
    )
    geo_restriction: Optional[GeoRestrictionConstraintType] = field(
        default=None,
        metadata={
            "name": "geoRestriction",
            "type": "Element",
        }
    )
    age_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "ageRating",
            "type": "Element",
        }
    )
    has_age_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasAgeRating",
            "type": "Element",
        }
    )
    content_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentRating",
            "type": "Element",
        }
    )
    has_content_rating: Optional[str] = field(
        default=None,
        metadata={
            "name": "hasContentRating",
            "type": "Element",
        }
    )
    genre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
