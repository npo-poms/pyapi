from dataclasses import dataclass, field
from typing import List, Optional
from .date_range_matcher_list_type import DateRangeMatcherListType
from .duration_range_matcher_list_type import DurationRangeMatcherListType
from .extended_text_matcher_list_type import ExtendedTextMatcherListType
from .geo_location_search_type import GeoLocationSearchType
from .match import Match
from .media_relation_search_list_type import MediaRelationSearchListType
from .schedule_event_search_type import ScheduleEventSearchType
from .simple_matcher_type import SimpleMatcherType
from .text_matcher_list_type import TextMatcherListType
from .title_search_type import TitleSearchType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaSearchType:
    """
    Limits the search result to media with certain properties.

    :ivar text:
    :ivar mediaIds: The MID must match one of the mediaIds
    :ivar types: The media type must match one of these.
    :ivar avTypes:
    :ivar sortDates:
    :ivar publishDates:
    :ivar creationDates:
    :ivar lastModifiedDates:
    :ivar broadcasters:
    :ivar locations:
    :ivar tags:
    :ivar genres:
    :ivar durations:
    :ivar descendantOf:
    :ivar episodeOf:
    :ivar memberOf:
    :ivar relations:
    :ivar scheduleEvents:
    :ivar ageRatings:
    :ivar contentRatings:
    :ivar titles:
    :ivar geoLocations:
    :ivar match:
    """
    class Meta:
        name = "mediaSearchType"

    text: Optional[SimpleMatcherType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mediaIds: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    avTypes: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sortDates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    publishDates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    creationDates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    lastModifiedDates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    locations: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    durations: Optional[DurationRangeMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    descendantOf: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    episodeOf: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    memberOf: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[MediaRelationSearchListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    scheduleEvents: List[ScheduleEventSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    ageRatings: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    contentRatings: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    titles: List[TitleSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    geoLocations: List[GeoLocationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
