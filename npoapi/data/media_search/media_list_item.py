from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from ..media.av_type_enum import AvTypeEnum
from ..media.location_type import LocationType
from ..media.media_type_enum import MediaTypeEnum
from ..media.organization_type import OrganizationType
from ..media.schedule_event_type import ScheduleEventType
from ..media.streaming_status import StreamingStatus
from ..media.tag_type import TagType
from .image_list_item import ImageListItem
from .publishable_list_item import PublishableListItem

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class MediaListItem(PublishableListItem):
    class Meta:
        name = "mediaListItem"

    broadcaster: List[OrganizationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
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
    subTitle: Optional[str] = field(
        default=None,
        metadata={
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
    creationDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    lastModified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    createdBy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    lastModifiedBy: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    sortDate: Optional[XmlDateTime] = field(
        default=None,
        metadata={
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
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    lastPublished: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    firstScheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    firstScheduleEventNoRerun: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    lastScheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    lastScheduleEventNoRerun: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    sortDateScheduleEvent: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
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
    numberOfLocations: Optional[int] = field(
        default=None,
        metadata={
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
    streamingPlatformStatus: Optional[StreamingStatus] = field(
        default=None,
        metadata={
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
    avType: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mediaType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    episodesLocked: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
