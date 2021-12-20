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
    avTypes: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sortDates: Optional[DateRangeFacetsType] = field(
        default=None,
        metadata={
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
    descendantOf: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    episodeOf: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    memberOf: Optional[MemberRefFacetType] = field(
        default=None,
        metadata={
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
    ageRatings: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    contentRatings: Optional[MediaFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    geoLocations: Optional[MediaSearchableTermFacetType] = field(
        default=None,
        metadata={
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
