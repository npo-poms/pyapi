from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlDuration
from npoapi.data.media import (
    BaseMediaType,
    ChannelEnum,
    GeoRoleType,
    Group,
    MediaTypeEnum,
    Program,
    ScheduleEventType,
    Segment,
    TextualTypeEnum,
)
from npoapi.data.shared import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class AbstractFacetType:
    class Meta:
        name = "abstractFacetType"


@dataclass
class DateRangeFacetItemType:
    class Meta:
        name = "dateRangeFacetItemType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


class DateRangePresetTypeEnum(Enum):
    BEFORE_LAST_YEAR = "BEFORE_LAST_YEAR"
    LAST_YEAR = "LAST_YEAR"
    LAST_MONTH = "LAST_MONTH"
    LAST_WEEK = "LAST_WEEK"
    YESTERDAY = "YESTERDAY"
    TODAY = "TODAY"
    THIS_WEEK = "THIS_WEEK"
    TOMORROW = "TOMORROW"


@dataclass
class DurationRangeFacetItemType:
    class Meta:
        name = "durationRangeFacetItemType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    begin: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ErrorType:
    class Meta:
        name = "errorType"

    message: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    classValue: List[str] = field(
        default_factory=list,
        metadata={
            "name": "class",
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    cause: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    otherElement: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
    testResult: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    status: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class FacetOrderTypeEnum(Enum):
    VALUE_ASC = "VALUE_ASC"
    VALUE_DESC = "VALUE_DESC"
    COUNT_ASC = "COUNT_ASC"
    COUNT_DESC = "COUNT_DESC"
    TERM = "TERM"
    REVERSE_TERM = "REVERSE_TERM"
    COUNT = "COUNT"
    REVERSE_COUNT = "REVERSE_COUNT"


@dataclass
class FacetResultItem:
    class Meta:
        name = "facetResultItem"

    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "required": True,
        }
    )
    selected: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class HighlightType:
    class Meta:
        name = "highlightType"

    body: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    term: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class Match(Enum):
    MUST = "MUST"
    SHOULD = "SHOULD"
    NOT = "NOT"


@dataclass
class MediaSearchResults:
    class Meta:
        name = "mediaSearchResults"


class MediaSortTypeEnum(Enum):
    TITLE = "title"
    SORT_DATE = "sortDate"
    PUBLISH_DATE = "publishDate"
    EPISODE = "episode"
    EPISODE_ADDED = "episodeAdded"
    MEMBER_ADDED = "memberAdded"
    MEMBER = "member"
    CREATION_DATE = "creationDate"
    LAST_MODIFIED = "lastModified"


class OrderTypeEnum(Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclass
class PageSearchResults:
    class Meta:
        name = "pageSearchResults"


class PageSortTypeEnum(Enum):
    SORT_DATE = "sortDate"
    LAST_MODIFIED = "lastModified"
    LAST_PUBLISHED = "lastPublished"
    CREATION_DATE = "creationDate"


@dataclass
class RedirectEntry:
    class Meta:
        name = "redirectEntry"
        namespace = "urn:vpro:api:2013"

    fromValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        }
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ultimate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    circular: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class SimpleMatchType(Enum):
    TEXT = "TEXT"


class StandardMatchType(Enum):
    TEXT = "TEXT"
    REGEX = "REGEX"
    WILDCARD = "WILDCARD"


@dataclass
class Suggestion:
    class Meta:
        name = "suggestion"
        namespace = "urn:vpro:api:2013"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )


class TotalQualifier(Enum):
    EQUAL_TO = "EQUAL_TO"
    APPROXIMATE = "APPROXIMATE"
    GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"
    MISSING = "MISSING"


@dataclass
class ChangeType:
    class Meta:
        name = "changeType"

    media: Optional[BaseMediaType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    publishDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    deleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    tail: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    revision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mergedTo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    realPublishDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DateRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "dateRangeFacetsType"

    intervalOrPresetOrRange: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "interval",
                    "type": str,
                    "namespace": "urn:vpro:api:2013",
                },
                {
                    "name": "preset",
                    "type": DateRangePresetTypeEnum,
                    "namespace": "urn:vpro:api:2013",
                },
                {
                    "name": "range",
                    "type": DateRangeFacetItemType,
                    "namespace": "urn:vpro:api:2013",
                },
            ),
        }
    )


@dataclass
class DurationRangeFacetsType(AbstractFacetType):
    class Meta:
        name = "durationRangeFacetsType"

    intervalOrRange: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "interval",
                    "type": str,
                    "namespace": "urn:vpro:api:2013",
                },
                {
                    "name": "range",
                    "type": DurationRangeFacetItemType,
                    "namespace": "urn:vpro:api:2013",
                },
            ),
        }
    )


@dataclass
class Error(ErrorType):
    class Meta:
        name = "error"
        namespace = "urn:vpro:api:2013"


@dataclass
class ExtendedMatcherType:
    class Meta:
        name = "extendedMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    fuzziness: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    matchType: Optional[StandardMatchType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    caseSensitive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeoLocationSearchType:
    class Meta:
        name = "geoLocationSearchType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MatcherList:
    class Meta:
        name = "matcherList"

    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaSortType:
    class Meta:
        name = "mediaSortType"

    value: Optional[MediaSortTypeEnum] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    order: Optional[OrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageSortType:
    class Meta:
        name = "pageSortType"

    value: Optional[PageSortTypeEnum] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    order: Optional[OrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RangeFacetResultItem(FacetResultItem):
    class Meta:
        name = "rangeFacetResultItem"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RangeMatcherType:
    class Meta:
        name = "rangeMatcherType"

    inclusiveEnd: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class RedirectList:
    class Meta:
        name = "redirectList"

    entry: List[RedirectEntry] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    lastUpdate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ResultType:
    class Meta:
        name = "resultType"

    items: Optional["ResultType.Items"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    total: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    totalQualifier: Optional[TotalQualifier] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Items:
        item: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:api:2013",
            }
        )


@dataclass
class ScheduleEventApiType(ScheduleEventType):
    class Meta:
        name = "scheduleEventApiType"

    program: Optional[Program] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    segment: Optional[Segment] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )


@dataclass
class SearchResultItem:
    class Meta:
        name = "searchResultItem"

    result: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: List[HighlightType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    score: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SimpleMatcherType:
    """
    :ivar value:
    :ivar fuzziness:
    :ivar semantic: Whether the search must happen via the semantic vectorization. This is beta feature, which
        may not be enabled.
    :ivar matchType:
    :ivar match:
    """
    class Meta:
        name = "simpleMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    fuzziness: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    semantic: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    matchType: Optional[SimpleMatchType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TermFacetResultItemType(FacetResultItem):
    class Meta:
        name = "termFacetResultItemType"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class TextFacetType(AbstractFacetType):
    class Meta:
        name = "textFacetType"

    threshold: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    include: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    script: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sort: Optional[FacetOrderTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TextMatcherType:
    class Meta:
        name = "textMatcherType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    matchType: Optional[StandardMatchType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TitleSearchType:
    class Meta:
        name = "titleSearchType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    matchType: Optional[StandardMatchType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Change(ChangeType):
    class Meta:
        name = "change"
        namespace = "urn:vpro:api:2013"


@dataclass
class DateFacetResultItemType(RangeFacetResultItem):
    class Meta:
        name = "dateFacetResultItemType"

    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DateRangeMatcherType(RangeMatcherType):
    class Meta:
        name = "dateRangeMatcherType"

    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationFacetResultItemType(RangeFacetResultItem):
    class Meta:
        name = "durationFacetResultItemType"

    begin: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationRangeMatcherType(RangeMatcherType):
    class Meta:
        name = "durationRangeMatcherType"

    begin: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ExtendedTextMatcherListType(MatcherList):
    class Meta:
        name = "extendedTextMatcherListType"

    matcher: List[ExtendedMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaGenreFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "mediaGenreFacetResultItemType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaGeoLocationFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "mediaGeoLocationFacetResultItemType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaResultType(ResultType):
    class Meta:
        name = "mediaResultType"


@dataclass
class MediaTitleFacetType(TextFacetType):
    class Meta:
        name = "mediaTitleFacetType"

    subSearch: Optional[TitleSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MemberRefFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "memberRefFacetResultItemType"

    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class NamedTermFacetResultItemType:
    class Meta:
        name = "namedTermFacetResultItemType"

    facet: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageGenreFacetResultItemType(TermFacetResultItemType):
    class Meta:
        name = "pageGenreFacetResultItemType"

    term: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageSortListType:
    class Meta:
        name = "pageSortListType"

    sort: List[PageSortType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )


@dataclass
class Redirects(RedirectList):
    class Meta:
        name = "redirects"
        namespace = "urn:vpro:api:2013"


@dataclass
class ScheduleEventSearchType(RangeMatcherType):
    class Meta:
        name = "scheduleEventSearchType"

    begin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    rerun: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ScheduleItem(ScheduleEventApiType):
    class Meta:
        name = "scheduleItem"
        namespace = "urn:vpro:api:2013"


@dataclass
class SearchResultType(ResultType):
    class Meta:
        name = "searchResultType"


@dataclass
class SuggestResultType(ResultType):
    class Meta:
        name = "suggestResultType"


@dataclass
class TextMatcherListType(MatcherList):
    class Meta:
        name = "textMatcherListType"

    matcher: List[TextMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class TitleSortOrderType(MediaSortType):
    class Meta:
        name = "titleSortOrderType"

    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    owner: Optional[OwnerTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AssociationSearchType:
    class Meta:
        name = "associationSearchType"

    urls: Optional[TextMatcherListType] = field(
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
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DateRangeMatcherListType(MatcherList):
    class Meta:
        name = "dateRangeMatcherListType"

    matcher: List[DateRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class DurationRangeMatcherListType(MatcherList):
    class Meta:
        name = "durationRangeMatcherListType"

    matcher: List[DurationRangeMatcherType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


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


@dataclass
class MediaRelationSearchType:
    class Meta:
        name = "mediaRelationSearchType"

    types: Optional[TextMatcherListType] = field(
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
    values: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    uriRefs: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaResult(MediaResultType):
    class Meta:
        name = "mediaResult"
        namespace = "urn:vpro:api:2013"


@dataclass
class MemberRefSearchType:
    class Meta:
        name = "memberRefSearchType"

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
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageFacetsResultType:
    class Meta:
        name = "pageFacetsResultType"

    sortDates: List[DateFacetResultItemType] = field(
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
    broadcasters: List[TermFacetResultItemType] = field(
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
    keywords: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    genres: List[PageGenreFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    portals: List[TermFacetResultItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
            "nillable": True,
        }
    )
    sections: List[TermFacetResultItemType] = field(
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


@dataclass
class PageRelationSearchType:
    class Meta:
        name = "pageRelationSearchType"

    types: Optional[TextMatcherListType] = field(
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
    values: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    uriRefs: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SubtitlesSearchType:
    class Meta:
        name = "subtitlesSearchType"

    text: Optional[SimpleMatcherType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mids: Optional[TextMatcherListType] = field(
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
    languages: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SuggestResult(SuggestResultType):
    class Meta:
        name = "suggestResult"
        namespace = "urn:vpro:api:2013"


@dataclass
class TermSearchType:
    class Meta:
        name = "termSearchType"

    ids: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GenericMediaSearchResultType(SearchResultType):
    class Meta:
        name = "genericMediaSearchResultType"

    facets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    selectedFacets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaRelationSearchListType:
    class Meta:
        name = "mediaRelationSearchListType"

    relationSearch: List[MediaRelationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageAssociationSearchListType:
    class Meta:
        name = "pageAssociationSearchListType"

    search: List[AssociationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageRelationSearchListType:
    class Meta:
        name = "pageRelationSearchListType"

    relationSearch: List[PageRelationSearchType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageSearchResultType(SearchResultType):
    class Meta:
        name = "pageSearchResultType"

    facets: Optional[PageFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    selectedFacets: Optional[PageFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mediaFacets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mediaSelectedFacets: Optional[MediaFacetsResultType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class SubtitlesFormType:
    class Meta:
        name = "subtitlesFormType"

    searches: Optional[SubtitlesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaSearchResultType(GenericMediaSearchResultType):
    class Meta:
        name = "mediaSearchResultType"


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


@dataclass
class PageSearchResult(PageSearchResultType):
    class Meta:
        name = "pageSearchResult"
        namespace = "urn:vpro:api:2013"


@dataclass
class PagesSearchType:
    class Meta:
        name = "pagesSearchType"

    text: Optional[SimpleMatcherType] = field(
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
    types: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    portals: Optional[TextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sections: Optional[TextMatcherListType] = field(
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
    tags: Optional[ExtendedTextMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    keywords: Optional[ExtendedTextMatcherListType] = field(
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
    lastModifiedDates: Optional[DateRangeMatcherListType] = field(
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
    publishDates: Optional[DateRangeMatcherListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[PageRelationSearchListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    links: Optional[PageAssociationSearchListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    referrals: Optional[PageAssociationSearchListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    match: Optional[Match] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SubtitlesForm(SubtitlesFormType):
    class Meta:
        name = "subtitlesForm"
        namespace = "urn:vpro:api:2013"


@dataclass
class ExtendedMediaFacetType(TextFacetType):
    class Meta:
        name = "extendedMediaFacetType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    caseSensitive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ExtendedPageFacetType(TextFacetType):
    class Meta:
        name = "extendedPageFacetType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    caseSensitive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaFacetType(TextFacetType):
    class Meta:
        name = "mediaFacetType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaSearchResult(MediaSearchResultType):
    class Meta:
        name = "mediaSearchResult"
        namespace = "urn:vpro:api:2013"


@dataclass
class PageFacetType(TextFacetType):
    class Meta:
        name = "pageFacetType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ScheduleFormType:
    class Meta:
        name = "scheduleFormType"

    searches: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaRelationFacetType(ExtendedMediaFacetType):
    class Meta:
        name = "mediaRelationFacetType"

    subSearch: Optional[MediaRelationSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MediaSearchableTermFacetType(MediaFacetType):
    class Meta:
        name = "mediaSearchableTermFacetType"

    subSearch: Optional[TermSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaTitleFacetListType(MediaFacetType):
    class Meta:
        name = "mediaTitleFacetListType"

    subSearch: Optional[TitleSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    title: List[MediaTitleFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MemberRefFacetType(MediaFacetType):
    class Meta:
        name = "memberRefFacetType"

    subSearch: Optional[MemberRefSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageRelationFacetType(ExtendedPageFacetType):
    class Meta:
        name = "pageRelationFacetType"

    subSearch: Optional[PageRelationSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PageSearchableTermFacetType(PageFacetType):
    class Meta:
        name = "pageSearchableTermFacetType"

    subSearch: Optional[TermSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class ScheduleForm(ScheduleFormType):
    class Meta:
        name = "scheduleForm"
        namespace = "urn:vpro:api:2013"


@dataclass
class MediaRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "mediaRelationFacetListType"

    filter: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    subSearch: Optional[MediaRelationSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facet: List[MediaRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class PageRelationFacetListType(AbstractFacetType):
    class Meta:
        name = "pageRelationFacetListType"

    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    subSearch: Optional[PageRelationSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facet: List[PageRelationFacetType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


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


@dataclass
class PagesFacetsType:
    class Meta:
        name = "pagesFacetsType"

    sortDates: Optional[DateRangeFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    broadcasters: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    types: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    tags: Optional[ExtendedPageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    keywords: Optional[ExtendedPageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    genres: Optional[PageSearchableTermFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    portals: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sections: Optional[PageFacetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    relations: Optional[PageRelationFacetListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    filter: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )


@dataclass
class MediaFormType:
    class Meta:
        name = "mediaFormType"

    searches: Optional[MediaSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sortFields: Optional["MediaFormType.SortFields"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: Optional[MediaFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class SortFields:
        sortOrTitleSort: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "sort",
                        "type": MediaSortType,
                        "namespace": "urn:vpro:api:2013",
                    },
                    {
                        "name": "titleSort",
                        "type": TitleSortOrderType,
                        "namespace": "urn:vpro:api:2013",
                    },
                ),
            }
        )


@dataclass
class MediaForm(MediaFormType):
    class Meta:
        name = "mediaForm"
        namespace = "urn:vpro:api:2013"


@dataclass
class PagesFormType:
    class Meta:
        name = "pagesFormType"

    searches: Optional[PagesSearchType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    sortFields: Optional[PageSortListType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    facets: Optional[PagesFacetsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    mediaForm: Optional[MediaForm] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:2013",
        }
    )
    highlight: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PagesForm(PagesFormType):
    class Meta:
        name = "pagesForm"
        namespace = "urn:vpro:api:2013"