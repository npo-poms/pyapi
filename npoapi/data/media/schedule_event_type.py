from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from .av_attributes_type import AvAttributesType
from .channel_enum import ChannelEnum
from .repeat_type import RepeatType
from .schedule_event_description import ScheduleEventDescription
from .schedule_event_title import ScheduleEventTitle
from .schedule_event_type_enum import ScheduleEventTypeEnum

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class ScheduleEventType:
    class Meta:
        name = "scheduleEventType"

    title: List[ScheduleEventTitle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    description: List[ScheduleEventDescription] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    repeat: Optional[RepeatType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    memberOf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    avAttributes: Optional[AvAttributesType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    textSubtitles: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    textPage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    guideDay: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
            "required": True,
        }
    )
    poProgId: Optional[str] = field(
        default=None,
        metadata={
            "name": "poProgID",
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    primaryLifestyle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    secondaryLifestyle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:2009",
        }
    )
    imi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    guideDayAttribute: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Attribute",
        }
    )
    midRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urnRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type: Optional[ScheduleEventTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
