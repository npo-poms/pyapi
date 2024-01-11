from dataclasses import dataclass, field
from typing import List, Optional, Type, Union
from npoapi.data.api_constraint import OperatorType
from npoapi.data.media import PlatformTypeEnum

__NAMESPACE__ = "urn:vpro:api:constraint:media:2013"


@dataclass(slots=True)
class HasAgeRatingConstraintType:
    class Meta:
        name = "hasAgeRatingConstraintType"


@dataclass(slots=True)
class HasContentRatingConstraintType:
    class Meta:
        name = "hasContentRatingConstraintType"


@dataclass(slots=True)
class HasGeoRestrictionConstraintType:
    class Meta:
        name = "hasGeoRestrictionConstraintType"


@dataclass(slots=True)
class HasImageConstraintType:
    class Meta:
        name = "hasImageConstraintType"


@dataclass(slots=True)
class HasLocationConstraintType:
    class Meta:
        name = "hasLocationConstraintType"

    platform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class HasPortalConstraintType:
    class Meta:
        name = "hasPortalConstraintType"


@dataclass(slots=True)
class HasPortalRestrictionConstraintType:
    class Meta:
        name = "hasPortalRestrictionConstraintType"


@dataclass(slots=True)
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
        },
    )
    exact: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class GeoRestrictionConstraintType:
    class Meta:
        name = "geoRestrictionConstraintType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class HasPredictionConstraintType:
    class Meta:
        name = "hasPredictionConstraintType"

    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class ScheduleEventType:
    """
    Documentation for schedule event date.

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
        },
    )
    operator: Optional[OperatorType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Not:
    class Meta:
        name = "not"

    choice: Optional[
        Union[
            "And",
            "Or",
            "Not",
            str,
            ProgramUrlConstraintType,
            HasImageConstraintType,
            HasLocationConstraintType,
            HasPredictionConstraintType,
            ScheduleEventType,
            HasPortalConstraintType,
            HasPortalRestrictionConstraintType,
            HasGeoRestrictionConstraintType,
            GeoRestrictionConstraintType,
            HasAgeRatingConstraintType,
            HasContentRatingConstraintType,
        ]
    ] = field(
        default=None,
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
                    "type": Type["Not"],
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
        },
    )


@dataclass(slots=True)
class Or:
    class Meta:
        name = "or"

    choice: List[
        Union[
            "And",
            "Or",
            Not,
            str,
            ProgramUrlConstraintType,
            HasImageConstraintType,
            HasLocationConstraintType,
            HasPredictionConstraintType,
            ScheduleEventType,
            HasPortalConstraintType,
            HasPortalRestrictionConstraintType,
            HasGeoRestrictionConstraintType,
            GeoRestrictionConstraintType,
            HasAgeRatingConstraintType,
            HasContentRatingConstraintType,
        ]
    ] = field(
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
        },
    )


@dataclass(slots=True)
class And:
    class Meta:
        name = "and"

    choice: List[
        Union[
            "And",
            Or,
            Not,
            str,
            ProgramUrlConstraintType,
            HasImageConstraintType,
            HasLocationConstraintType,
            HasPredictionConstraintType,
            ScheduleEventType,
            HasPortalConstraintType,
            HasPortalRestrictionConstraintType,
            HasGeoRestrictionConstraintType,
            GeoRestrictionConstraintType,
            HasAgeRatingConstraintType,
            HasContentRatingConstraintType,
        ]
    ] = field(
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
        },
    )


@dataclass(slots=True)
class Filter:
    class Meta:
        name = "filter"
        namespace = "urn:vpro:api:constraint:media:2013"

    choice: Optional[
        Union[
            And,
            Or,
            Not,
            str,
            ProgramUrlConstraintType,
            HasImageConstraintType,
            HasLocationConstraintType,
            HasPredictionConstraintType,
            ScheduleEventType,
            HasPortalConstraintType,
            HasPortalRestrictionConstraintType,
            HasGeoRestrictionConstraintType,
            GeoRestrictionConstraintType,
            HasAgeRatingConstraintType,
            HasContentRatingConstraintType,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "and",
                    "type": And,
                },
                {
                    "name": "or",
                    "type": Or,
                },
                {
                    "name": "not",
                    "type": Not,
                },
                {
                    "name": "avType",
                    "type": str,
                },
                {
                    "name": "avFileFormat",
                    "type": str,
                },
                {
                    "name": "avFileExtension",
                    "type": str,
                },
                {
                    "name": "programUrl",
                    "type": ProgramUrlConstraintType,
                },
                {
                    "name": "descendantOf",
                    "type": str,
                },
                {
                    "name": "broadcaster",
                    "type": str,
                },
                {
                    "name": "hasImage",
                    "type": HasImageConstraintType,
                },
                {
                    "name": "hasLocation",
                    "type": HasLocationConstraintType,
                },
                {
                    "name": "hasPrediction",
                    "type": HasPredictionConstraintType,
                },
                {
                    "name": "type",
                    "type": str,
                },
                {
                    "name": "channel",
                    "type": str,
                },
                {
                    "name": "scheduleEvent",
                    "type": ScheduleEventType,
                },
                {
                    "name": "hasPortal",
                    "type": HasPortalConstraintType,
                },
                {
                    "name": "portal",
                    "type": str,
                },
                {
                    "name": "isExclusive",
                    "type": HasPortalRestrictionConstraintType,
                },
                {
                    "name": "exclusive",
                    "type": str,
                },
                {
                    "name": "hasGeoRestriction",
                    "type": HasGeoRestrictionConstraintType,
                },
                {
                    "name": "geoRestriction",
                    "type": GeoRestrictionConstraintType,
                },
                {
                    "name": "ageRating",
                    "type": str,
                },
                {
                    "name": "hasAgeRating",
                    "type": HasAgeRatingConstraintType,
                },
                {
                    "name": "contentRating",
                    "type": str,
                },
                {
                    "name": "hasContentRating",
                    "type": HasContentRatingConstraintType,
                },
                {
                    "name": "genre",
                    "type": str,
                },
            ),
        },
    )
