from dataclasses import dataclass, field
from typing import List
from .date_facet_result_item_type import DateFacetResultItemType
from .duration_facet_result_item_type import DurationFacetResultItemType
from .media_genre_facet_result_item_type import MediaGenreFacetResultItemType
from .media_geo_location_facet_result_item_type import MediaGeoLocationFacetResultItemType
from .member_ref_facet_result_item_type import MemberRefFacetResultItemType
from .named_term_facet_result_item_type import NamedTermFacetResultItemType
from .term_facet_result_item_type import TermFacetResultItemType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class MediaFacetsResultType:
    class Meta:
        name = "mediaFacetsResultType"

    titles: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    types: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    avTypes: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    sortDates: List[DateFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    broadcasters: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    genres: List[MediaGenreFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    geoLocations: List[MediaGeoLocationFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    tags: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    durations: List[DurationFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    descendantOf: List[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    episodeOf: List[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    memberOf: List[MemberRefFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    relations: List[NamedTermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    ageRatings: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    contentRatings: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
