from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
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


@dataclass
class DateRangeValueType:
    """
    :ivar value:
    :ivar inclusive:
    """
    class Meta:
        name = "dateRangeValueType"

    value: Optional[str] = field(
        default=None,
    )
    inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EditorSearch:
    """
    :ivar value:
    :ivar principal_id:
    """
    class Meta:
        name = "editorSearch"

    value: Optional[str] = field(
        default=None,
    )
    principal_id: Optional[bool] = field(
        default=None,
        metadata={
            "name": "principalId",
            "type": "Attribute",
        }
    )


@dataclass
class IntegerRangeValueType:
    """
    :ivar value:
    :ivar inclusive:
    """
    class Meta:
        name = "integerRangeValueType"

    value: Optional[int] = field(
        default=None,
    )
    inclusive: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class MediaSortField(Enum):
    """
    :cvar SORT_TITLE:
    :cvar MID:
    :cvar TYPE:
    :cvar MEDIA_TYPE:
    :cvar SORT_DATE:
    :cvar LAST_MODIFIED:
    :cvar CREATION_DATE:
    :cvar PUBLISH_STOP:
    :cvar PUBLISH_START:
    :cvar LAST_PUBLISHED:
    :cvar LAST_MODIFIED_BY:
    :cvar CREATED_BY:
    :cvar LOCATIONS:
    :cvar MEMBEROF_COUNT:
    :cvar EPISODEOF_COUNT:
    """
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


@dataclass
class RelationFormType:
    """
    :ivar value:
    :ivar type:
    :ivar broadcaster:
    :ivar uri_ref:
    """
    class Meta:
        name = "relationFormType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
    uri_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriRef",
            "type": "Attribute",
        }
    )


@dataclass
class DateRangeType:
    """
    :ivar start:
    :ivar stop:
    """
    class Meta:
        name = "dateRangeType"

    start: Optional[DateRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    stop: Optional[DateRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )


@dataclass
class IntegerRangeType:
    """
    :ivar start:
    :ivar stop:
    """
    class Meta:
        name = "integerRangeType"

    start: Optional[IntegerRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    stop: Optional[IntegerRangeValueType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )


@dataclass
class MediaPagerType:
    """
    :ivar offset:
    :ivar max:
    :ivar sort:
    :ivar order:
    """
    class Meta:
        name = "mediaPagerType"

    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "min_inclusive": 0,
        }
    )
    max: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
            "min_inclusive": 0,
        }
    )
    sort: Optional[MediaSortField] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    order: Optional["MediaPagerType.Order"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )

    class Order(Enum):
        """
        :cvar ASC:
        :cvar DESC:
        """
        ASC = "ASC"
        DESC = "DESC"


@dataclass
class PublishableListItem:
    """
    :ivar id:
    :ivar urn:
    :ivar workflow:
    :ivar deleted:
    """
    class Meta:
        name = "publishableListItem"

    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    workflow: Optional[WorkflowEnumType] = field(
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


@dataclass
class ImageListItem(PublishableListItem):
    class Meta:
        name = "imageListItem"


@dataclass
class MediaFormType:
    """
    :ivar pager:
    :ivar broadcaster:
    :ivar portal:
    :ivar organization:
    :ivar text:
    :ivar title:
    :ivar type:
    :ivar release_year:
    :ivar relation:
    :ivar no_broadcast:
    :ivar schedule_events_count:
    :ivar has_locations: Whether it should only return media object which does have location. Note that the same can be accomplished with 'locationsCount', and this element is considered deprecated.
    :ivar locations_count: Constraint the number of locations.
    :ivar no_playlist: Whether it should only return media object which are not a a member of any other object.
                Note that the same can be accomplished with 'memberOfCount', and this element is considered deprecated.
    :ivar member_of_count:
    :ivar sort_range:
    :ivar event_range:
    :ivar schedule_event_range:
    :ivar channel:
    :ivar net:
    :ivar created_by:
    :ivar creation_range:
    :ivar last_modified_by:
    :ivar last_modified_range:
    :ivar last_published_range:
    :ivar tag:
    :ivar av_type:
    :ivar not_an_episode:
    :ivar episode_of_count:
    :ivar no_members:
    :ivar no_credits:
    :ivar images_without_credits_count:
    :ivar images_count:
    :ivar find_deleted:
    :ivar excluded_mid:
    :ivar ids:
    :ivar descendant_of:
    :ivar streaming_platform_status:
    """
    class Meta:
        name = "mediaFormType"

    pager: Optional[MediaPagerType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    organization: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    title: List["MediaFormType.Title"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    type: List[MediaTypeEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    release_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "releaseYear",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    relation: Optional[RelationFormType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    no_broadcast: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noBroadcast",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    schedule_events_count: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "scheduleEventsCount",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    has_locations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "hasLocations",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    locations_count: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "locationsCount",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    no_playlist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noPlaylist",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    member_of_count: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "memberOfCount",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    sort_range: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "name": "sortRange",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    event_range: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "name": "eventRange",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    schedule_event_range: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "name": "scheduleEventRange",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    channel: List[ChannelEnum] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    net: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    created_by: Optional[EditorSearch] = field(
        default=None,
        metadata={
            "name": "createdBy",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    creation_range: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "name": "creationRange",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    last_modified_by: Optional[EditorSearch] = field(
        default=None,
        metadata={
            "name": "lastModifiedBy",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    last_modified_range: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "name": "lastModifiedRange",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    last_published_range: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "name": "lastPublishedRange",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    av_type: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "name": "avType",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    not_an_episode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "notAnEpisode",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    episode_of_count: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "episodeOfCount",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    no_members: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noMembers",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    no_credits: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noCredits",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    images_without_credits_count: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "imagesWithoutCreditsCount",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    images_count: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "name": "imagesCount",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    find_deleted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "findDeleted",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    excluded_mid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "excludedMid",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    ids: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    descendant_of: List[str] = field(
        default_factory=list,
        metadata={
            "name": "descendantOf",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    streaming_platform_status: List[StreamingStatus] = field(
        default_factory=list,
        metadata={
            "name": "streamingPlatformStatus",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )

    @dataclass
    class Title:
        """
        :ivar value:
        :ivar type:
        :ivar owner:
        :ivar tokenized:
        """
        value: Optional[str] = field(
            default=None,
        )
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
        tokenized: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class MediaForm(MediaFormType):
    class Meta:
        name = "mediaForm"
        namespace = "urn:vpro:media:search:2012"


@dataclass
class MediaListItem(PublishableListItem):
    """
    :ivar broadcaster:
    :ivar title:
    :ivar sub_title:
    :ivar description:
    :ivar creation_date:
    :ivar last_modified:
    :ivar created_by:
    :ivar last_modified_by:
    :ivar sort_date:
    :ivar type:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar last_published:
    :ivar first_schedule_event:
    :ivar locations:
    :ivar number_of_locations:
    :ivar tag:
    :ivar image:
    :ivar streaming_platform_status:
    :ivar mid:
    :ivar av_type:
    :ivar media_type:
    :ivar episodes_locked:
    """
    class Meta:
        name = "mediaListItem"

    broadcaster: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "min_occurs": 1,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    sub_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "subTitle",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    creation_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    created_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "createdBy",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    last_modified_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastModifiedBy",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    sort_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "sortDate",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    last_published: Optional[str] = field(
        default=None,
        metadata={
            "name": "lastPublished",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    first_schedule_event: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "name": "firstScheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    locations: List[LocationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "nillable": True,
        }
    )
    number_of_locations: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfLocations",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    tag: List[TagType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    image: Optional[ImageListItem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    streaming_platform_status: Optional[StreamingStatus] = field(
        default=None,
        metadata={
            "name": "streamingPlatformStatus",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    av_type: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "name": "avType",
            "type": "Attribute",
        }
    )
    media_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mediaType",
            "type": "Attribute",
        }
    )
    episodes_locked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "episodesLocked",
            "type": "Attribute",
        }
    )


@dataclass
class MediaListResultType:
    """
    :ivar item:
    :ivar total_count:
    :ivar offset:
    :ivar max:
    :ivar size:
    :ivar sort:
    :ivar order:
    """
    class Meta:
        name = "mediaListResultType"

    item: List[MediaListItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    total_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalCount",
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
    size: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    sort: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    order: Optional["MediaListResultType.Order"] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    class Order(Enum):
        """
        :cvar ASC:
        :cvar DESC:
        """
        ASC = "ASC"
        DESC = "DESC"


@dataclass
class ListType(MediaListResultType):
    class Meta:
        name = "list"
        namespace = "urn:vpro:media:search:2012"
