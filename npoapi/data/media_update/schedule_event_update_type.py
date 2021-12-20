from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
from ..media.channel_enum import ChannelEnum
from .description_update_type import DescriptionUpdateType
from .title_update_type import TitleUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class ScheduleEventUpdateType:
    class Meta:
        name = "scheduleEventUpdateType"

    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    guideDay: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    titles: Optional["ScheduleEventUpdateType.Titles"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    descriptions: Optional["ScheduleEventUpdateType.Descriptions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Titles:
        title: List[TitleUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class Descriptions:
        description: List[DescriptionUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )
