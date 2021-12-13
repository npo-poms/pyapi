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
    :ivar media_ids: The MID must match one of the mediaIds
    :ivar types: The media type must match one of these.
    :ivar av_types:
    :ivar sort_dates:
    :ivar publish_dates:
    :ivar creation_dates:
    :ivar last_modified_dates:
    :ivar broadcasters:
    :ivar locations:
    :ivar tags:
    :ivar genres:
    :ivar durations:
    :ivar descendant_of:
    :ivar episode_of:
    :ivar member_of:
    :ivar relations:
    :ivar schedule_events:
    :ivar age_ratings:
    :ivar content_ratings:
    :ivar titles:
    :ivar geo_locations:
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
    media_ids: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "mediaIds",
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
    av_types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    publish_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "publishDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    creation_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "creationDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    last_modified_dates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "name": "lastModifiedDates",
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
    descendant_of: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    episode_of: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    member_of: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "memberOf",
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
    schedule_events: List[ScheduleEventSearchType] = field(
        default_factory=list,
        metadata={
            "name": "scheduleEvents",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    age_ratings: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    content_ratings: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "name": "contentRatings",
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
    geo_locations: List[GeoLocationSearchType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocations",
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
