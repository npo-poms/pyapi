from dataclasses import dataclass, field
from typing import List, Optional, Type
from .geo_restriction_constraint_type import GeoRestrictionConstraintType
from .has_age_rating_constraint_type import HasAgeRatingConstraintType
from .has_content_rating_constraint_type import HasContentRatingConstraintType
from .has_geo_restriction_constraint_type import HasGeoRestrictionConstraintType
from .has_image_constraint_type import HasImageConstraintType
from .has_location_constraint_type import HasLocationConstraintType
from .has_portal_constraint_type import HasPortalConstraintType
from .has_portal_restriction_constraint_type import HasPortalRestrictionConstraintType
from .has_prediction_constraint_type import HasPredictionConstraintType
from .program_url_constraint_type import ProgramUrlConstraintType
from .schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class Not:
    class Meta:
        name = "not"

    andValue: Optional["And"] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    orValue: Optional["Or"] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    notValue: Optional["Not"] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    avType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    avFileFormat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    avFileExtension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    programUrl: Optional[ProgramUrlConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    descendantOf: Optional[str] = field(
        default=None,
        metadata={
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
    hasImage: Optional[HasImageConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    hasLocation: Optional[HasLocationConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    hasPrediction: Optional[HasPredictionConstraintType] = field(
        default=None,
        metadata={
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
    scheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    hasPortal: Optional[HasPortalConstraintType] = field(
        default=None,
        metadata={
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
    isExclusive: Optional[HasPortalRestrictionConstraintType] = field(
        default=None,
        metadata={
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
    hasGeoRestriction: Optional[HasGeoRestrictionConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    geoRestriction: Optional[GeoRestrictionConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    ageRating: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    hasAgeRating: Optional[HasAgeRatingConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    contentRating: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    hasContentRating: Optional[HasContentRatingConstraintType] = field(
        default=None,
        metadata={
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
class Or:
    class Meta:
        name = "or"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "and",
                    "type": Type["And"],
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "or",
                    "type": Type["Or"],
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "not",
                    "type": Not,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "avType",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "avFileFormat",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "avFileExtension",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "programUrl",
                    "type": ProgramUrlConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "descendantOf",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "broadcaster",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasImage",
                    "type": HasImageConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasLocation",
                    "type": HasLocationConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasPrediction",
                    "type": HasPredictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "type",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "channel",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "scheduleEvent",
                    "type": ScheduleEventType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasPortal",
                    "type": HasPortalConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "portal",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "isExclusive",
                    "type": HasPortalRestrictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "exclusive",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasGeoRestriction",
                    "type": HasGeoRestrictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "geoRestriction",
                    "type": GeoRestrictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "ageRating",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasAgeRating",
                    "type": HasAgeRatingConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "contentRating",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasContentRating",
                    "type": HasContentRatingConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "genre",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
            ),
        }
    )


@dataclass
class And:
    class Meta:
        name = "and"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "and",
                    "type": Type["And"],
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "or",
                    "type": Or,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "not",
                    "type": Not,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "avType",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "avFileFormat",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "avFileExtension",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "programUrl",
                    "type": ProgramUrlConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "descendantOf",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "broadcaster",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasImage",
                    "type": HasImageConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasLocation",
                    "type": HasLocationConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasPrediction",
                    "type": HasPredictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "type",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "channel",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "scheduleEvent",
                    "type": ScheduleEventType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasPortal",
                    "type": HasPortalConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "portal",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "isExclusive",
                    "type": HasPortalRestrictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "exclusive",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasGeoRestriction",
                    "type": HasGeoRestrictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "geoRestriction",
                    "type": GeoRestrictionConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "ageRating",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasAgeRating",
                    "type": HasAgeRatingConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "contentRating",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "hasContentRating",
                    "type": HasContentRatingConstraintType,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
                {
                    "name": "genre",
                    "type": str,
                    "namespace": "urn:vpro:api:constraint:media:2013",
                },
            ),
        }
    )
