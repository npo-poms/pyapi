from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from npoapi.data.media import (
    AvTypeEnum,
    ChannelEnum,
    LocationType,
    MediaTypeEnum,
    OrganizationType,
    ScheduleEventType,
    StreamingStatus,
    TagType,
    TextualTypeEnum,
)
from npoapi.data.shared import (
    OwnerTypeEnum,
    WorkflowEnumType,
)

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass(slots=True)
class DateRangeValueType:
    class Meta:
        name = "dateRangeValueType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class EditorSearch:
    class Meta:
        name = "editorSearch"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    principalId: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class IntegerRangeValueType:
    class Meta:
        name = "integerRangeValueType"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class MediaListResultTypeOrder(Enum):
    ASC = "ASC"
    DESC = "DESC"


class MediaPagerTypeOrder(Enum):
    ASC = "ASC"
    DESC = "DESC"


class MediaSortField(Enum):
    SORT_TITLE = "sortTitle"
    MID = "mid"
    TYPE = "type"
    MEDIA_TYPE = "mediaType"
    SORT_DATE = "sortDate"
    LAST_MODIFIED = "lastModified"
    CREATION_DATE = "creationDate"
    PUBLISH_STOP = "publishStop"
    PUBLISH_START = "publishStart"
    LAST_PUBLISHED = "lastPublished"
    LAST_MODIFIED_BY = "lastModifiedBy"
    CREATED_BY = "createdBy"
    LOCATIONS = "locations"
    MEMBEROF_COUNT = "memberofCount"
    EPISODEOF_COUNT = "episodeofCount"


@dataclass(slots=True)
class RelationFormType:
    class Meta:
        name = "relationFormType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    typeValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z0-9_-]{2,}",
        },
    )
    uriRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class DateRangeType:
    class Meta:
        name = "dateRangeType"

    start: Optional[DateRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    stop: Optional[DateRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )


@dataclass(slots=True)
class IntegerRangeType:
    class Meta:
        name = "integerRangeType"

    start: Optional[IntegerRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    stop: Optional[IntegerRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )


@dataclass(slots=True)
class MediaPagerType:
    class Meta:
        name = "mediaPagerType"

    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "min_inclusive": 0,
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
            "min_inclusive": 0,
        },
    )
    sort: Optional[MediaSortField] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    order: Optional[MediaPagerTypeOrder] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )


@dataclass(slots=True)
class PublishableListItem:
    class Meta:
        name = "publishableListItem"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    workflow: Optional[WorkflowEnumType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    deleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class ImageListItem(PublishableListItem):
    class Meta:
        name = "imageListItem"


@dataclass(slots=True)
class MediaFormType:
    """
    :ivar pager:
    :ivar broadcaster:
    :ivar portal:
    :ivar organization:
    :ivar text:
    :ivar title:
    :ivar typeValue:
    :ivar releaseYear:
    :ivar relation:
    :ivar noBroadcast:
    :ivar scheduleEventsCount:
    :ivar hasLocations: Whether it should only return media object which does have location. Note that the same
        can be accomplished with 'locationsCount', and this element is considered deprecated.
    :ivar locationsCount: Constraint the number of locations.
    :ivar noPlaylist: Whether it should only return media object which are not a a member of any other object.
        Note that the same can be accomplished with 'memberOfCount', and this element is considered deprecated.
    :ivar memberOfCount:
    :ivar sortRange:
    :ivar eventRange:
    :ivar scheduleEventRange:
    :ivar channel:
    :ivar net:
    :ivar createdBy:
    :ivar creationRange:
    :ivar lastModifiedBy:
    :ivar lastModifiedRange:
    :ivar lastPublishedRange:
    :ivar tag:
    :ivar avType:
    :ivar notAnEpisode:
    :ivar episodeOfCount:
    :ivar noMembers:
    :ivar noCredits:
    :ivar imagesWithoutCreditsCount:
    :ivar imagesCount:
    :ivar findDeleted:
    :ivar excludedMid:
    :ivar ids:
    :ivar descendantOf:
    :ivar streamingPlatformStatus:
    """

    class Meta:
        name = "mediaFormType"

    pager: Optional[MediaPagerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        },
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    organization: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "pattern": r"[A-Z0-9_-]{2,}",
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    title: List["MediaFormType.Title"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    typeValue: List[MediaTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    releaseYear: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    relation: Optional[RelationFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    noBroadcast: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    scheduleEventsCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    hasLocations: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    locationsCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    noPlaylist: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    memberOfCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    sortRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    eventRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    scheduleEventRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    channel: List[ChannelEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    net: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    createdBy: Optional[EditorSearch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    creationRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    lastModifiedBy: Optional[EditorSearch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    lastModifiedRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    lastPublishedRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    avType: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    notAnEpisode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    episodeOfCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    noMembers: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    noCredits: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    imagesWithoutCreditsCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    imagesCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    findDeleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    excludedMid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    ids: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    descendantOf: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    streamingPlatformStatus: List[StreamingStatus] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )

    @dataclass(slots=True)
    class Title:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        typeValue: Optional[TextualTypeEnum] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
            },
        )
        owner: Optional[OwnerTypeEnum] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        tokenized: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(slots=True)
class MediaForm(MediaFormType):
    class Meta:
        name = "mediaForm"
        namespace = "urn:vpro:media:search:2012"


@dataclass(slots=True)
class MediaListItem(PublishableListItem):
    class Meta:
        name = "mediaListItem"

    broadcaster: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    subTitle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    creationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        },
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    createdBy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        },
    )
    lastModifiedBy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    sortDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    typeValue: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    lastPublished: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    firstScheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    firstScheduleEventNoRerun: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    lastScheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    lastScheduleEventNoRerun: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    sortDateScheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    locations: List[LocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "nillable": True,
        },
    )
    numberOfLocations: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    numberOfPublishedLocations: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    tag: List[TagType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    image: Optional[ImageListItem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    streamingPlatformStatus: Optional[StreamingStatus] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    avType: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mediaType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    episodesLocked: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class MediaListResultType:
    class Meta:
        name = "mediaListResultType"

    item: List[MediaListItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        },
    )
    totalCount: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    sort: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    order: Optional[MediaListResultTypeOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class ListType(MediaListResultType):
    class Meta:
        name = "list"
        namespace = "urn:vpro:media:search:2012"
