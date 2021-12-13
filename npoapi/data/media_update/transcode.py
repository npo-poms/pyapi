from dataclasses import dataclass
from .transcode_type import TranscodeType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Transcode(TranscodeType):
    class Meta:
        name = "transcode"
        namespace = "urn:vpro:media:update:2009"
