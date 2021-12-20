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
    releaseYear: Optional[int] = field(
        default=None,
        metadata={
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
    noBroadcast: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    scheduleEventsCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    hasLocations: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    locationsCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    noPlaylist: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    memberOfCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    sortRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    eventRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    scheduleEventRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
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
    createdBy: Optional[EditorSearch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    creationRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    lastModifiedBy: Optional[EditorSearch] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    lastModifiedRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    lastPublishedRange: Optional[DateRangeType] = field(
        default=None,
        metadata={
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
    avType: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    notAnEpisode: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    episodeOfCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    noMembers: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    noCredits: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    imagesWithoutCreditsCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    imagesCount: Optional[IntegerRangeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    findDeleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    excludedMid: List[str] = field(
        default_factory=list,
        metadata={
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
    descendantOf: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    streamingPlatformStatus: List[StreamingStatus] = field(
        default_factory=list,
        metadata={
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
