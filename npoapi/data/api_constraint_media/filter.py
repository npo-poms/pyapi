from dataclasses import dataclass, field
from typing import Optional
from .geo_restriction_constraint_type import GeoRestrictionConstraintType
from .has_age_rating_constraint_type import HasAgeRatingConstraintType
from .has_content_rating_constraint_type import HasContentRatingConstraintType
from .has_geo_restriction_constraint_type import HasGeoRestrictionConstraintType
from .has_image_constraint_type import HasImageConstraintType
from .has_location_constraint_type import HasLocationConstraintType
from .has_portal_constraint_type import HasPortalConstraintType
from .has_portal_restriction_constraint_type import HasPortalRestrictionConstraintType
from .has_prediction_constraint_type import HasPredictionConstraintType
from .not_mod import (
    And,
    Not,
    Or,
)
from .program_url_constraint_type import ProgramUrlConstraintType
from .schedule_event_type import ScheduleEventType

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass
class Filter:
    class Meta:
        name = "filter"
        namespace = "urn:vpro:api:constraint:media:2013"

    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        }
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        }
    )
    not_value: Optional[Not] = field(
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
    has_image: Optional[HasImageConstraintType] = field(
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
    has_portal: Optional[HasPortalConstraintType] = field(
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
    is_exclusive: Optional[HasPortalRestrictionConstraintType] = field(
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
    has_geo_restriction: Optional[HasGeoRestrictionConstraintType] = field(
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
    has_age_rating: Optional[HasAgeRatingConstraintType] = field(
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
    has_content_rating: Optional[HasContentRatingConstraintType] = field(
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
