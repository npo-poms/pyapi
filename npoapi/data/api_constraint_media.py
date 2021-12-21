from dataclasses import dataclass, field
from typing import List, Optional, Type
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
    """
    Constraints on the program url field of locations.
    """
    class Meta:
        name = "programUrlConstraintType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    exact: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeoRestrictionConstraintType:
    class Meta:
        name = "geoRestrictionConstraintType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class HasPredictionConstraintType:
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
    """
    documentation for schedule event date.

    :ivar date: A timestamp spec. This is parsed by the natty parser. Try out with
        http://natty.joestelmach.com/try.jsp
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
