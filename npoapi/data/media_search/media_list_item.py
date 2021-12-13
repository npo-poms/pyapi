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
    creation_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "creationDate",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
            "required": True,
        }
    )
    last_modified: Optional[XmlDateTime] = field(
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
    sort_date: Optional[XmlDateTime] = field(
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
    publish_start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    publish_stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    last_published: Optional[XmlDateTime] = field(
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
    first_schedule_event_no_rerun: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "name": "firstScheduleEventNoRerun",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    last_schedule_event: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "name": "lastScheduleEvent",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    last_schedule_event_no_rerun: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "name": "lastScheduleEventNoRerun",
            "type": "Element",
            "namespace": "urn:vpro:media:search:2012",
        }
    )
    sort_date_schedule_event: Optional[ScheduleEventType] = field(
        default=None,
        metadata={
            "name": "sortDateScheduleEvent",
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
