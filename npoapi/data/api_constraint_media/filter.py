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

    andValue: Optional[And] = field(
        default=None,
        metadata={
            "name": "and",
            "type": "Element",
        }
    )
    orValue: Optional[Or] = field(
        default=None,
        metadata={
            "name": "or",
            "type": "Element",
        }
    )
    notValue: Optional[Not] = field(
        default=None,
        metadata={
            "name": "not",
            "type": "Element",
        }
    )
    avType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    avFileFormat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    avFileExtension: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    programUrl: Optional[ProgramUrlConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    descendantOf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hasImage: Optional[HasImageConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hasLocation: Optional[HasLocationConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hasPrediction: Optional[HasPredictionConstraintType] = field(
        default=None,
        metadata={
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
    scheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hasPortal: Optional[HasPortalConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    portal: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    isExclusive: Optional[HasPortalRestrictionConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    exclusive: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hasGeoRestriction: Optional[HasGeoRestrictionConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    geoRestriction: Optional[GeoRestrictionConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ageRating: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hasAgeRating: Optional[HasAgeRatingConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    contentRating: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    hasContentRating: Optional[HasContentRatingConstraintType] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    genre: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
