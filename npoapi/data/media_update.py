from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from npoapi.data.media import (
    AgeRatingType,
    AspectRatioEnum,
    AvFileFormatEnum,
    AvTypeEnum,
    ChannelEnum,
    ColorType,
    ContentRatingType,
    Encryption,
    GeoRestrictionEnum,
    GeoRoleType,
    GroupTypeEnum,
    IntentionEnum,
    MediaTypeEnum,
    PlatformTypeEnum,
    ProgramTypeEnum,
    RoleType,
    SegmentTypeEnum,
    TargetGroupEnum,
    TextualTypeEnum,
)
from npoapi.data.shared import (
    ImageTypeEnum,
    LicenseEnum,
)

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class AssetDataType:
    """
    :ivar data:
    """
    class Meta:
        name = "assetDataType"

    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )


@dataclass
class AssetLocationType:
    """
    :ivar url:
    """
    class Meta:
        name = "assetLocationType"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )


@dataclass
class AudioAttributesUpdateType:
    """
    :ivar channels:
    :ivar coding:
    """
    class Meta:
        name = "audioAttributesUpdateType"

    channels: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    coding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass
class ImageDataType:
    """
    :ivar data:
    """
    class Meta:
        name = "imageDataType"

    data: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )


@dataclass
class ImageLocationType:
    """
    :ivar mime_type: Sometimes it may be usefull to explicitely specify the mimetype of the given location. (E.g. if there are no or no correct http content type headers).
    :ivar url:
    """
    class Meta:
        name = "imageLocationType"

    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "max_length": 1024,
            "pattern": r"[a-z][a-z]+:.*",
        }
    )


@dataclass
class ItemizeType:
    """
    :ivar start:
    :ivar stop:
    :ivar mid:
    """
    class Meta:
        name = "itemizeType"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    stop: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ListType:
    """
    :ivar any_element:
    :ivar offset:
    :ivar total_count:
    :ivar max:
    :ivar size:
    :ivar order:
    """
    class Meta:
        name = "list"
        namespace = "urn:vpro:media:update:2009"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    total_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "totalCount",
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
    order: Optional["ListType.Order"] = field(
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
class LiveItemize1:
    """
    :ivar start:
    :ivar stop:
    :ivar stream:
    """
    class Meta:
        name = "liveItemize"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    stop: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    stream: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MemberRefUpdateType:
    """
    :ivar value:
    :ivar position:
    :ivar highlighted:
    """
    class Meta:
        name = "memberRefUpdateType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 4,
        }
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MemberUpdateType:
    """
    :ivar any_element:
    :ivar position:
    :ivar highlighted:
    """
    class Meta:
        name = "memberUpdateType"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    highlighted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MoveActionType:
    """
    :ivar from_value:
    :ivar to:
    """
    class Meta:
        name = "moveActionType"

    from_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    to: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )


@dataclass
class PortalRestrictionUpdateType:
    """
    :ivar value:
    :ivar start:
    :ivar stop:
    """
    class Meta:
        name = "portalRestrictionUpdateType"

    value: Optional[str] = field(
        default=None,
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class PriorityType(Enum):
    """
    :cvar LOW:
    :cvar NORMAL:
    :cvar HIGH:
    :cvar URGENT:
    """
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    URGENT = "URGENT"


@dataclass
class RelationUpdateType:
    """
    :ivar value:
    :ivar type:
    :ivar broadcaster:
    :ivar uri_ref:
    :ivar urn:
    """
    class Meta:
        name = "relationUpdateType"

    value: Optional[str] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Z0-9_-]{4,}",
        }
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    uri_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "uriRef",
            "type": "Attribute",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TopicUpdateType:
    """
    :ivar gtaa_uri:
    """
    class Meta:
        name = "topicUpdateType"

    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
            "required": True,
        }
    )


class TranscodeStatusEnum(Enum):
    """
    :cvar RUNNING:
    :cvar COMPLETED:
    :cvar FAILED:
    :cvar TIMED_OUT:
    :cvar TERMINATED:
    :cvar PAUSED:
    """
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    TERMINATED = "TERMINATED"
    PAUSED = "PAUSED"


@dataclass
class AssetType:
    """
    :ivar asset_data:
    :ivar asset_location:
    :ivar publish_start:
    :ivar publish_stop:
    """
    class Meta:
        name = "assetType"

    asset_data: Optional[AssetDataType] = field(
        default=None,
        metadata={
            "name": "assetData",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    asset_location: Optional[AssetLocationType] = field(
        default=None,
        metadata={
            "name": "assetLocation",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )


@dataclass
class DescriptionUpdateType:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "descriptionUpdateType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class GeoLocationUpdateType:
    """
    :ivar gtaa_uri:
    :ivar role:
    """
    class Meta:
        name = "geoLocationUpdateType"

    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class GeoRestrictionUpdateType:
    """
    :ivar value:
    :ivar start:
    :ivar stop:
    :ivar platform:
    """
    class Meta:
        name = "geoRestrictionUpdateType"

    value: Optional[GeoRestrictionEnum] = field(
        default=None,
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    stop: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ImageUpdateType:
    """
    :ivar title:
    :ivar description:
    :ivar source: The source of the image. This is only metadata. It must be URL from where the image was originally acquired.
    :ivar source_name: A simple string representing the source of the image. E.g. 'flickr'.
    :ivar license:
    :ivar width:
    :ivar height:
    :ivar credits:
    :ivar date:
    :ivar offset:
    :ivar image_data: The image as a base-64 encoded blob.
    :ivar image_location: An URL from where the image can be downloaded from.
    :ivar urn: The URN of an already existing image inside the POMS image server.
    :ivar type:
    :ivar urn_attribute:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar highlighted:
    """
    class Meta:
        name = "imageUpdateType"

    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    source_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    image_data: Optional[ImageDataType] = field(
        default=None,
        metadata={
            "name": "imageData",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    image_location: Optional[ImageLocationType] = field(
        default=None,
        metadata={
            "name": "imageLocation",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"urn:vpro[\.:]image:[0-9]+",
        }
    )
    type: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    urn_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "urn",
            "type": "Attribute",
        }
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Itemize(ItemizeType):
    class Meta:
        name = "itemize"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class ItemizeResponseType:
    """
    :ivar request:
    :ivar liverequest:
    :ivar result:
    :ivar id:
    :ivar success:
    """
    class Meta:
        name = "itemizeResponseType"

    request: Optional[ItemizeType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    liverequest: Optional[LiveItemize1] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    result: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Liveitemize(LiveItemize1):
    class Meta:
        name = "liveitemize"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class MemberRef(MemberRefUpdateType):
    class Meta:
        name = "memberRef"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class MemberUpdate(MemberUpdateType):
    class Meta:
        name = "memberUpdate"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class MidAndTypeType:
    """
    :ivar crid:
    :ivar mid:
    :ivar id:
    :ivar type:
    """
    class Meta:
        name = "midAndTypeType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Move(MoveActionType):
    class Meta:
        name = "move"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class NameUpdateType:
    """
    :ivar gtaa_uri:
    :ivar role:
    """
    class Meta:
        name = "nameUpdateType"

    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
            "required": True,
        }
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PersonUpdateType:
    """
    :ivar given_name:
    :ivar family_name:
    :ivar gtaa_uri:
    :ivar role:
    """
    class Meta:
        name = "personUpdateType"

    given_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "givenName",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    family_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "familyName",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    gtaa_uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "gtaaUri",
            "type": "Attribute",
        }
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PredictionUpdateType:
    """
    :ivar value:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar encryption:
    """
    class Meta:
        name = "predictionUpdateType"

    value: Optional[PlatformTypeEnum] = field(
        default=None,
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    encryption: Optional[Encryption] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TitleUpdateType:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "titleUpdateType"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 1,
            "max_length": 255,
        }
    )
    type: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TopicsUpdateType:
    """
    :ivar topic:
    """
    class Meta:
        name = "topicsUpdateType"

    topic: List[TopicUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )


@dataclass
class TranscodeStatusType:
    """
    :ivar file_name:
    :ivar status:
    :ivar status_message:
    :ivar workflow_type:
    :ivar workflow_id:
    :ivar start_time:
    :ivar update_time:
    :ivar end_time:
    :ivar broadcasters:
    :ivar mid:
    :ivar missing_media:
    """
    class Meta:
        name = "transcodeStatusType"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    status: Optional[TranscodeStatusEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    status_message: Optional[str] = field(
        default=None,
        metadata={
            "name": "statusMessage",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    workflow_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "workflowType",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    workflow_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "workflowId",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "startTime",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    update_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "updateTime",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "endTime",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    broadcasters: Optional["TranscodeStatusType.Broadcasters"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    missing_media: Optional[bool] = field(
        default=None,
        metadata={
            "name": "missingMedia",
            "type": "Attribute",
        }
    )

    @dataclass
    class Broadcasters:
        """
        :ivar broadcaster:
        """
        broadcaster: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )


@dataclass
class TranscodeType:
    """
    :ivar file_name:
    :ivar encryption:
    :ivar priority:
    :ivar mid:
    """
    class Meta:
        name = "transcodeType"

    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    encryption: Optional[Encryption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    priority: Optional[PriorityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class VideoAttributesUpdateType:
    """
    :ivar aspect_ratio:
    :ivar color:
    :ivar coding:
    :ivar width:
    :ivar height:
    """
    class Meta:
        name = "videoAttributesUpdateType"

    aspect_ratio: Optional[AspectRatioEnum] = field(
        default=None,
        metadata={
            "name": "aspectRatio",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    coding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class AvAtributeUpdateType:
    """
    :ivar bitrate:
    :ivar byte_size:
    :ivar av_file_format:
    :ivar video_attributes:
    :ivar audio_attributes:
    """
    class Meta:
        name = "avAtributeUpdateType"

    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    byte_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "byteSize",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    av_file_format: Optional[AvFileFormatEnum] = field(
        default=None,
        metadata={
            "name": "avFileFormat",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    video_attributes: Optional[VideoAttributesUpdateType] = field(
        default=None,
        metadata={
            "name": "videoAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    audio_attributes: Optional[AudioAttributesUpdateType] = field(
        default=None,
        metadata={
            "name": "audioAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )


@dataclass
class BulkUpdateType:
    """
    :ivar titles:
    :ivar descriptions:
    """
    class Meta:
        name = "bulkUpdateType"

    titles: Optional[TitleUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    descriptions: Optional[DescriptionUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )


@dataclass
class CreditsUpdateType:
    """
    :ivar person:
    :ivar name:
    """
    class Meta:
        name = "creditsUpdateType"

    person: List[PersonUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "sequential": True,
        }
    )
    name: List[NameUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "sequential": True,
        }
    )


@dataclass
class GeoLocationsUpdateType:
    """
    :ivar geo_location:
    """
    class Meta:
        name = "geoLocationsUpdateType"

    geo_location: List[GeoLocationUpdateType] = field(
        default_factory=list,
        metadata={
            "name": "geoLocation",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )


@dataclass
class Image(ImageUpdateType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class ItemizeResponse(ItemizeResponseType):
    class Meta:
        name = "itemizeResponse"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class MidAndType(MidAndTypeType):
    class Meta:
        name = "midAndType"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class Prediction(PredictionUpdateType):
    class Meta:
        name = "prediction"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class ScheduleEventUpdateType:
    """
    :ivar start:
    :ivar guide_day:
    :ivar duration:
    :ivar titles:
    :ivar descriptions:
    :ivar channel:
    :ivar net:
    """
    class Meta:
        name = "scheduleEventUpdateType"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    guide_day: Optional[str] = field(
        default=None,
        metadata={
            "name": "guideDay",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    duration: Optional[str] = field(
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
        """
        :ivar title:
        """
        title: List[TitleUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class Descriptions:
        """
        :ivar description:
        """
        description: List[DescriptionUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )


@dataclass
class Transcode(TranscodeType):
    class Meta:
        name = "transcode"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class TranscodeStatus(TranscodeStatusType):
    class Meta:
        name = "transcodeStatus"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class LocationUpdateType:
    """
    :ivar program_url:
    :ivar av_attributes:
    :ivar offset:
    :ivar duration:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar urn:
    """
    class Meta:
        name = "locationUpdateType"

    program_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "programUrl",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    av_attributes: Optional[AvAtributeUpdateType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    offset: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Location(LocationUpdateType):
    class Meta:
        name = "location"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class MediaUpdateType:
    """
    :ivar crid:
    :ivar broadcaster:
    :ivar portal:
    :ivar exclusive:
    :ivar region:
    :ivar title: Titles in dutch
    :ivar description: Descriptions in dutch
    :ivar tag:
    :ivar country: Countries somehow associated with this item. This does not refer to the used language in the meta fields of
                this object. Only supported if version &gt;= 5.0.
    :ivar language: Languages somehow associated with this item. This does not refer to the used language in the meta fields of this object. They should be in dutch. Only supported if version &gt;= 5.0.
    :ivar genre:
    :ivar intentions:
    :ivar target_groups:
    :ivar geo_locations:
    :ivar topics:
    :ivar av_attributes:
    :ivar release_year:
    :ivar duration:
    :ivar credits:
    :ivar member_of:
    :ivar age_rating:
    :ivar content_rating:
    :ivar email:
    :ivar website:
    :ivar twitterref: Only supported if version &gt;= 5.10.
    :ivar prediction: With predictions it can be indicated for which platforms locations will be available.
                If there is a prediction for a certain platform, but the mediaobject is not yet available on the streaming platform, then
                there will be no associated location for that certain platform.

                If the streaming platform status changes, then according to these 'prediction' records the locations will be changed.
    :ivar locations:
    :ivar schedule_events: Please note that this is only available for program upates (since 5.11)
    :ivar relation:
    :ivar images:
    :ivar asset:
    :ivar av_type:
    :ivar deleted:
    :ivar embeddable:
    :ivar publish_start:
    :ivar publish_stop:
    :ivar mid:
    :ivar urn:
    :ivar ordered:
    :ivar version: The POMS version this XML applies too. This is optional, though some feature will only be supported if you explicitely specify a version which is big enough (To ensure backward compatiblity).
    """
    class Meta:
        name = "mediaUpdateType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        }
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_occurs": 1,
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"[A-Z0-9_-]{2,}",
        }
    )
    exclusive: List[PortalRestrictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    region: List[GeoRestrictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    title: List[TitleUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_occurs": 1,
        }
    )
    description: List[DescriptionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    country: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"3(\.[0-9]+)+",
        }
    )
    intentions: Optional["MediaUpdateType.Intentions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    target_groups: Optional["MediaUpdateType.TargetGroups"] = field(
        default=None,
        metadata={
            "name": "targetGroups",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    geo_locations: Optional[GeoLocationsUpdateType] = field(
        default=None,
        metadata={
            "name": "geoLocations",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    topics: Optional[TopicsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    av_attributes: Optional[AvAtributeUpdateType] = field(
        default=None,
        metadata={
            "name": "avAttributes",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    release_year: Optional[int] = field(
        default=None,
        metadata={
            "name": "releaseYear",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    duration: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    credits: Optional[CreditsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    member_of: List[MemberRefUpdateType] = field(
        default_factory=list,
        metadata={
            "name": "memberOf",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    age_rating: Optional[AgeRatingType] = field(
        default=None,
        metadata={
            "name": "ageRating",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    content_rating: List[ContentRatingType] = field(
        default_factory=list,
        metadata={
            "name": "contentRating",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    website: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    twitterref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 2,
            "max_length": 16,
            "pattern": r"[@#][A-Za-z0-9_]{1,139}",
        }
    )
    prediction: List[PredictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    locations: Optional["MediaUpdateType.Locations"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    schedule_events: Optional["MediaUpdateType.ScheduleEvents"] = field(
        default=None,
        metadata={
            "name": "scheduleEvents",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    relation: List[RelationUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    images: Optional["MediaUpdateType.Images"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    asset: Optional[AssetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    av_type: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "name": "avType",
            "type": "Attribute",
            "required": True,
        }
    )
    deleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    embeddable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    publish_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStart",
            "type": "Attribute",
        }
    )
    publish_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "publishStop",
            "type": "Attribute",
        }
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        }
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+(\.[0-9]+(\.[0-9]+)?)?",
        }
    )

    @dataclass
    class Intentions:
        """
        :ivar intention:
        """
        intention: List[IntentionEnum] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class TargetGroups:
        """
        :ivar target_group:
        """
        target_group: List[TargetGroupEnum] = field(
            default_factory=list,
            metadata={
                "name": "targetGroup",
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class Locations:
        """
        :ivar location:
        """
        location: List[LocationUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class ScheduleEvents:
        """
        :ivar schedule_event:
        """
        schedule_event: List[ScheduleEventUpdateType] = field(
            default_factory=list,
            metadata={
                "name": "scheduleEvent",
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )

    @dataclass
    class Images:
        """
        :ivar image:
        """
        image: List[ImageUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )


@dataclass
class GroupUpdateType(MediaUpdateType):
    """
    :ivar po_series_id:
    :ivar type:
    """
    class Meta:
        name = "groupUpdateType"

    po_series_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "poSeriesID",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        }
    )
    type: Optional[GroupTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SegmentUpdateType(MediaUpdateType):
    """
    :ivar start:
    :ivar mid_ref:
    :ivar type:
    """
    class Meta:
        name = "segmentUpdateType"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        }
    )
    mid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "midRef",
            "type": "Attribute",
        }
    )
    type: Optional[SegmentTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Group(GroupUpdateType):
    class Meta:
        name = "group"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class Segment(SegmentUpdateType):
    class Meta:
        name = "segment"
        namespace = "urn:vpro:media:update:2009"


@dataclass
class ProgramUpdateType(MediaUpdateType):
    """
    :ivar episode_of: episodeOf works similar to memberOf. Important differences: only programs of type CLIP or BROADCAST can
                    be an episode of a group and the group can only be of type SERIES or SEASON.
    :ivar segments: Optional list of program segments. A segment is a part of a program that can be visually shown on the
                    timeline of a player. A segment always has a start time indicating the start of the segment relative to
                    the parent program. A segment can have the same fields as other media objects, like titles, descriptions,
                    images, locations, etc.

                    The standard scenario when playing a segment is to load a location of the parent media object and
                    to use the start time as an offset to start playing the segment. However, it is also possible for a
                    segment to have its own locations. This makes it possible to for instance have a podcast of a weekly
                    segment in a radio show without providing the complete radio program it is a part of.

                    Rules:
                    - Start time is required
                    - If duration is not set the player should play until the end of the program
                    - Removing a program also deletes its segments
    :ivar type:
    """
    class Meta:
        name = "programUpdateType"

    episode_of: List[MemberRefUpdateType] = field(
        default_factory=list,
        metadata={
            "name": "episodeOf",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    segments: Optional["ProgramUpdateType.Segments"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        }
    )
    type: Optional[ProgramTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Segments:
        """
        :ivar segment:
        """
        segment: List[Segment] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            }
        )


@dataclass
class Program(ProgramUpdateType):
    class Meta:
        name = "program"
        namespace = "urn:vpro:media:update:2009"
