from dataclasses import dataclass, field
from typing import Optional
from .date_range_facets_type import DateRangeFacetsType
from .duration_range_facets_type import DurationRangeFacetsType
from .extended_media_facet_type import ExtendedMediaFacetType
from .media_facet_type import MediaFacetType
from .media_relation_facet_list_type import MediaRelationFacetListType
from .media_search_type import MediaSearchType
from .media_searchable_term_facet_type import MediaSearchableTermFacetType
from .media_title_facet_list_type import MediaTitleFacetListType
from .member_ref_facet_type import MemberRefFacetType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFacetsType:
    class Meta:
        name = "mediaFacetsType"

    titles: Optional[MediaTitleFacetListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    types: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    av_types: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "name": "avTypes",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort_dates: Optional[DateRangeFacetsType] = field(
        default=None,
        metadata={
            "name": "sortDates",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[MediaSearchableTermFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedMediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    durations: Optional[DurationRangeFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    descendant_of: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    episode_of: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    member_of: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[MediaRelationFacetListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    age_ratings: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "name": "ageRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    content_ratings: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "name": "contentRatings",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    geo_locations: Optional[MediaSearchableTermFacetType] = field(
        default=None,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
