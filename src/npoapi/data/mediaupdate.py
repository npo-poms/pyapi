from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime, XmlDuration
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


@dataclass(slots=True)
class AssetDataType:
    class Meta:
        name = "assetDataType"

    data: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "format": "base64",
        },
    )


@dataclass(slots=True)
class AssetLocationType:
    class Meta:
        name = "assetLocationType"

    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )


@dataclass(slots=True)
class AudioAttributesUpdateType:
    class Meta:
        name = "audioAttributesUpdateType"

    channels: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    coding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        },
    )


@dataclass(slots=True)
class ImageDataType:
    class Meta:
        name = "imageDataType"

    data: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "format": "base64",
        },
    )


@dataclass(slots=True)
class ImageLocationType:
    """
    :ivar mimeType: Sometimes it may be usefull to explicitely specify the mimetype of the given location. (E.g.
        if there are no or no correct http content type headers).
    :ivar url:
    """

    class Meta:
        name = "imageLocationType"

    mimeType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "max_length": 1024,
            "pattern": r"[a-z][a-z]+:.*",
        },
    )


@dataclass(slots=True)
class ItemizeType:
    class Meta:
        name = "itemizeType"

    start: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    stop: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ListOrder(Enum):
    ASC = "ASC"
    DESC = "DESC"


@dataclass(slots=True)
class LiveItemize1:
    class Meta:
        name = "liveItemize"

    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    stream: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class MemberRefUpdateType:
    class Meta:
        name = "memberRefUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 4,
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class MemberUpdateType:
    class Meta:
        name = "memberUpdateType"

    anyElement: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    position: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    highlighted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class MoveActionTypeType(Enum):
    """
    :cvar REFERENCE: 'from' and 'to' refer to mediaobjects in the list by reference (e.g. mid).
    :cvar NUMBER: Would refer to the number in the memberref object
    :cvar REF_ID: Refers to the id of the memberref object
    :cvar INDEX: 'from' and 'to' refer to the index (offset 0) of the mediaobject in the list.
    """

    REFERENCE = "REFERENCE"
    NUMBER = "NUMBER"
    REF_ID = "REF_ID"
    INDEX = "INDEX"


@dataclass(slots=True)
class PortalRestrictionUpdateType:
    class Meta:
        name = "portalRestrictionUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class PriorityType(Enum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"
    URGENT = "URGENT"


@dataclass(slots=True)
class RelationUpdateType:
    class Meta:
        name = "relationUpdateType"

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
            "required": True,
            "pattern": r"[A-Z0-9_-]{4,}",
        },
    )
    broadcaster: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    uriRef: Optional[str] = field(
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


@dataclass(slots=True)
class RepeatType:
    class Meta:
        name = "repeatType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    isRerun: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class TopicUpdateType:
    class Meta:
        name = "topicUpdateType"

    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


class TranscodeStatusEnum(Enum):
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    TIMED_OUT = "TIMED_OUT"
    TERMINATED = "TERMINATED"
    PAUSED = "PAUSED"


@dataclass(slots=True)
class UploadResponseType:
    class Meta:
        name = "uploadResponseType"

    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    response: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    bytes: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    statusCode: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class AssetType:
    class Meta:
        name = "assetType"

    assetDataOrAssetLocation: Optional[Union[AssetDataType, AssetLocationType]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "assetData",
                    "type": AssetDataType,
                    "namespace": "urn:vpro:media:update:2009",
                },
                {
                    "name": "assetLocation",
                    "type": AssetLocationType,
                    "namespace": "urn:vpro:media:update:2009",
                },
            ),
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class DescriptionUpdateType:
    class Meta:
        name = "descriptionUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
        },
    )
    typeValue: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class GeoLocationUpdateType:
    class Meta:
        name = "geoLocationUpdateType"

    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    role: Optional[GeoRoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class GeoRestrictionUpdateType:
    class Meta:
        name = "geoRestrictionUpdateType"

    value: Optional[GeoRestrictionEnum] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    stop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    platform: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class ImageUpdateType:
    """
    :ivar title:
    :ivar description:
    :ivar source: The source of the image. This is only metadata. It must be URL from where the image was
        originally acquired.
    :ivar sourceName: A simple string representing the source of the image. E.g. 'flickr'.
    :ivar license:
    :ivar width:
    :ivar height:
    :ivar credits:
    :ivar date:
    :ivar offset:
    :ivar imageDataOrImageLocationOrUrn:
    :ivar typeValue:
    :ivar urnAttribute:
    :ivar publishStart:
    :ivar publishStop:
    :ivar highlighted:
    :ivar delete: If true, the image will be marked deleted.
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
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    sourceName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    license: Optional[LicenseEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    credits: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    imageDataOrImageLocationOrUrn: Optional[Union[ImageDataType, ImageLocationType, str]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "imageData",
                    "type": ImageDataType,
                    "namespace": "urn:vpro:media:update:2009",
                },
                {
                    "name": "imageLocation",
                    "type": ImageLocationType,
                    "namespace": "urn:vpro:media:update:2009",
                },
                {
                    "name": "urn",
                    "type": str,
                    "namespace": "urn:vpro:media:update:2009",
                    "pattern": r"urn:vpro[\.:]image:[0-9]+",
                },
            ),
        },
    )
    typeValue: Optional[ImageTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    urnAttribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "urn",
            "type": "Attribute",
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    highlighted: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    delete: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Itemize(ItemizeType):
    class Meta:
        name = "itemize"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class ItemizeResponseType:
    class Meta:
        name = "itemizeResponseType"

    requestOrLiverequest: Optional[Union[ItemizeType, LiveItemize1]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "request",
                    "type": ItemizeType,
                    "namespace": "urn:vpro:media:update:2009",
                },
                {
                    "name": "liverequest",
                    "type": LiveItemize1,
                    "namespace": "urn:vpro:media:update:2009",
                },
            ),
        },
    )
    result: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class ListType:
    class Meta:
        name = "list"
        namespace = "urn:vpro:media:update:2009"

    anyElement: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    offset: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    totalCount: Optional[int] = field(
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
    order: Optional[ListOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Liveitemize(LiveItemize1):
    class Meta:
        name = "liveitemize"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class MemberRef(MemberRefUpdateType):
    class Meta:
        name = "memberRef"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class MemberUpdate(MemberUpdateType):
    class Meta:
        name = "memberUpdate"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class MidAndTypeType:
    class Meta:
        name = "midAndTypeType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        },
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    typeValue: Optional[MediaTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class MoveActionType:
    class Meta:
        name = "moveActionType"

    fromValue: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    typeValue: Optional[MoveActionTypeType] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class NameUpdateType:
    class Meta:
        name = "nameUpdateType"

    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class PersonUpdateType:
    class Meta:
        name = "personUpdateType"

    givenName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    familyName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    gtaaUri: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    role: Optional[RoleType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class PredictionUpdateType:
    class Meta:
        name = "predictionUpdateType"

    value: Optional[PlatformTypeEnum] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    encryption: Optional[Encryption] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class TitleUpdateType:
    class Meta:
        name = "titleUpdateType"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    typeValue: Optional[TextualTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class TopicsUpdateType:
    class Meta:
        name = "topicsUpdateType"

    topic: List[TopicUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )


@dataclass(slots=True)
class TranscodeStatusType:
    class Meta:
        name = "transcodeStatusType"

    fileName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    status: Optional[TranscodeStatusEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    statusMessage: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    workflowType: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    workflowId: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    startTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    updateTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    endTime: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    broadcasters: Optional["TranscodeStatusType.Broadcasters"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    missingMedia: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(slots=True)
    class Broadcasters:
        broadcaster: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )


@dataclass(slots=True)
class TranscodeType:
    class Meta:
        name = "transcodeType"

    fileName: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    encryption: Optional[Encryption] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    priority: Optional[PriorityType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class UploadResponse(UploadResponseType):
    class Meta:
        name = "uploadResponse"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class VideoAttributesUpdateType:
    class Meta:
        name = "videoAttributesUpdateType"

    aspectRatio: Optional[AspectRatioEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    color: Optional[ColorType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    coding: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        },
    )
    width: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    height: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class AvAtributeUpdateType:
    class Meta:
        name = "avAtributeUpdateType"

    bitrate: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    byteSize: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    avFileFormat: Optional[AvFileFormatEnum] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    videoAttributes: Optional[VideoAttributesUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    audioAttributes: Optional[AudioAttributesUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )


@dataclass(slots=True)
class BulkUpdateType:
    class Meta:
        name = "bulkUpdateType"

    titles: Optional[TitleUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    descriptions: Optional[DescriptionUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )


@dataclass(slots=True)
class CreditsUpdateType:
    class Meta:
        name = "creditsUpdateType"

    personOrName: List[Union[PersonUpdateType, NameUpdateType]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "person",
                    "type": PersonUpdateType,
                    "namespace": "urn:vpro:media:update:2009",
                },
                {
                    "name": "name",
                    "type": NameUpdateType,
                    "namespace": "urn:vpro:media:update:2009",
                },
            ),
        },
    )


@dataclass(slots=True)
class GeoLocationsUpdateType:
    class Meta:
        name = "geoLocationsUpdateType"

    geoLocation: List[GeoLocationUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )


@dataclass(slots=True)
class Image(ImageUpdateType):
    class Meta:
        name = "image"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class ItemizeResponse(ItemizeResponseType):
    class Meta:
        name = "itemizeResponse"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class MidAndType(MidAndTypeType):
    class Meta:
        name = "midAndType"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class Move(MoveActionType):
    class Meta:
        name = "move"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class Prediction(PredictionUpdateType):
    class Meta:
        name = "prediction"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class ScheduleEventUpdateType:
    class Meta:
        name = "scheduleEventUpdateType"

    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    guideDay: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    repeat: Optional[RepeatType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    titles: Optional["ScheduleEventUpdateType.Titles"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    descriptions: Optional["ScheduleEventUpdateType.Descriptions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    channel: Optional[ChannelEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    net: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(slots=True)
    class Titles:
        title: List[TitleUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )

    @dataclass(slots=True)
    class Descriptions:
        description: List[DescriptionUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )


@dataclass(slots=True)
class Transcode(TranscodeType):
    class Meta:
        name = "transcode"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class TranscodeStatus(TranscodeStatusType):
    class Meta:
        name = "transcodeStatus"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class LocationUpdateType:
    """
    :ivar programUrl:
    :ivar avAttributes:
    :ivar offset:
    :ivar duration:
    :ivar publishStart:
    :ivar publishStop:
    :ivar urn:
    :ivar delete: If true, the location will be marked deleted.
    """

    class Meta:
        name = "locationUpdateType"

    programUrl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    avAttributes: Optional[AvAtributeUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    offset: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
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
    delete: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Location(LocationUpdateType):
    class Meta:
        name = "location"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
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
    :ivar country: Countries somehow associated with this item. This does not refer to the used language in the
        meta fields of this object. Only supported if version &gt;= 5.0.
    :ivar language: Languages somehow associated with this item. This does not refer to the used language in the
        meta fields of this object. They should be in dutch. Only supported if version &gt;= 5.0.
    :ivar genre:
    :ivar intentions:
    :ivar targetGroups:
    :ivar geoLocations:
    :ivar topics:
    :ivar avAttributes:
    :ivar releaseYear:
    :ivar duration:
    :ivar credits:
    :ivar memberOf:
    :ivar ageRating:
    :ivar contentRating:
    :ivar email:
    :ivar website:
    :ivar twitterref: Only supported if version &gt;= 5.10.
    :ivar prediction: With predictions it can be indicated for which platforms locations will be available. If
        there is a prediction for a certain platform, but the mediaobject is not yet available on the streaming
        platform, then there will be no associated location for that certain platform. If the streaming platform
        status changes, then according to these 'prediction' records the locations will be changed.
    :ivar locations:
    :ivar scheduleEvents: Please note that this is only available for program upates (since 5.11)
    :ivar relation:
    :ivar images:
    :ivar asset:
    :ivar avType:
    :ivar deleted:
    :ivar embeddable:
    :ivar publishStart:
    :ivar publishStop:
    :ivar mid:
    :ivar urn:
    :ivar ordered:
    :ivar version: <xs:paragraphs xmlns:xs="http://www.w3.org/2001/XMLSchema"> The POMS version this XML applies
        too. This is optional, though some features will only be supported if you explicitly specify a version
        which is big enough (To ensure backward compatibility). If you don't specify it,  there will be no
        backwards compatibility. </xs:paragraphs>
    """

    class Meta:
        name = "mediaUpdateType"

    crid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"(c|C)(r|R)(i|I)(d|D)://.*/.*",
        },
    )
    broadcaster: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_occurs": 1,
            "pattern": r"[A-Z0-9_-]{2,}",
        },
    )
    portal: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"[A-Z0-9_-]{2,}",
        },
    )
    exclusive: List[PortalRestrictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    region: List[GeoRestrictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    title: List[TitleUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_occurs": 1,
        },
    )
    description: List[DescriptionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    tag: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        },
    )
    country: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    genre: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "pattern": r"3(\.[0-9]+)+",
        },
    )
    intentions: Optional["MediaUpdateType.Intentions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    targetGroups: Optional["MediaUpdateType.TargetGroups"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    geoLocations: Optional[GeoLocationsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    topics: Optional[TopicsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    avAttributes: Optional[AvAtributeUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    releaseYear: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    credits: Optional[CreditsUpdateType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    memberOf: List[MemberRefUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    ageRating: Optional[AgeRatingType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    contentRating: List[ContentRatingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    email: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        },
    )
    website: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        },
    )
    twitterref: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 2,
            "max_length": 16,
            "pattern": r"[@#][A-Za-z0-9_]{1,139}",
        },
    )
    prediction: List[PredictionUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    locations: Optional["MediaUpdateType.Locations"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    scheduleEvents: Optional["MediaUpdateType.ScheduleEvents"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    relation: List[RelationUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    images: Optional["MediaUpdateType.Images"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    asset: Optional[AssetType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    avType: Optional[AvTypeEnum] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    deleted: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    embeddable: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    publishStart: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    publishStop: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 4,
            "max_length": 255,
            "pattern": r"[ \.a-zA-Z0-9_-]+",
        },
    )
    urn: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ordered: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]+(\.[0-9]+(\.[0-9]+)?)?",
        },
    )

    @dataclass(slots=True)
    class Intentions:
        intention: List[IntentionEnum] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )

    @dataclass(slots=True)
    class TargetGroups:
        targetGroup: List[TargetGroupEnum] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )

    @dataclass(slots=True)
    class Locations:
        location: List[LocationUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )

    @dataclass(slots=True)
    class ScheduleEvents:
        scheduleEvent: List[ScheduleEventUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )

    @dataclass(slots=True)
    class Images:
        image: List[ImageUpdateType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )


@dataclass(slots=True)
class GroupUpdateType(MediaUpdateType):
    class Meta:
        name = "groupUpdateType"

    poSeriesId: Optional[str] = field(
        default=None,
        metadata={
            "name": "poSeriesID",
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "min_length": 1,
            "max_length": 255,
        },
    )
    typeValue: Optional[GroupTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(slots=True)
class SegmentUpdateType(MediaUpdateType):
    class Meta:
        name = "segmentUpdateType"

    start: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
            "required": True,
        },
    )
    midRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    typeValue: Optional[SegmentTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass(slots=True)
class Group(GroupUpdateType):
    class Meta:
        name = "group"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class Segment(SegmentUpdateType):
    class Meta:
        name = "segment"
        namespace = "urn:vpro:media:update:2009"


@dataclass(slots=True)
class ProgramUpdateType(MediaUpdateType):
    """
    :ivar episodeOf: episodeOf works similar to memberOf. Important differences: only programs of type CLIP or
        BROADCAST can be an episode of a group and the group can only be of type SERIES or SEASON.
    :ivar segments: Optional list of program segments. A segment is a part of a program that can be visually
        shown on the timeline of a player. A segment always has a start time indicating the start of the segment
        relative to the parent program. A segment can have the same fields as other media objects, like titles,
        descriptions, images, locations, etc. The standard scenario when playing a segment is to load a location
        of the parent media object and to use the start time as an offset to start playing the segment. However,
        it is also possible for a segment to have its own locations. This makes it possible to for instance have
        a podcast of a weekly segment in a radio show without providing the complete radio program it is a part
        of. Rules: - Start time is required - If duration is not set the player should play until the end of the
        program - Removing a program also deletes its segments
    :ivar typeValue:
    """

    class Meta:
        name = "programUpdateType"

    episodeOf: List[MemberRefUpdateType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    segments: Optional["ProgramUpdateType.Segments"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:media:update:2009",
        },
    )
    typeValue: Optional[ProgramTypeEnum] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )

    @dataclass(slots=True)
    class Segments:
        segment: List[Segment] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:vpro:media:update:2009",
            },
        )


@dataclass(slots=True)
class Program(ProgramUpdateType):
    class Meta:
        name = "program"
        namespace = "urn:vpro:media:update:2009"
