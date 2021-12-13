from dataclasses import dataclass
from .transcode_status_type import TranscodeStatusType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class TranscodeStatus(TranscodeStatusType):
    class Meta:
        name = "transcodeStatus"
        namespace = "urn:vpro:media:update:2009"
