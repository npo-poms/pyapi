from dataclasses import dataclass, field
from typing import List, Optional
from ..media.av_type_enum import AvTypeEnum
from ..media.channel_enum import ChannelEnum
from ..media.media_type_enum import MediaTypeEnum
from ..media.streaming_status import StreamingStatus
from ..media.textual_type_enum import TextualTypeEnum
from .date_range_type import DateRangeType
from .editor_search import EditorSearch
from .integer_range_type import IntegerRangeType
from .media_pager_type import MediaPagerType
from .relation_form_type import RelationFormType
from ..shared.owner_type_enum import OwnerTypeEnum

__NAMESPACE__ = "urn:vpro:media:search:2012"


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
    :ivar has_locations: Whether it should only return media object which does have location. Note that the same
        can be accomplished with 'locationsCount', and this element is considered deprecated.
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
        value: str = field(
            default="",
            metadata={
                "required": True,
            }
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
