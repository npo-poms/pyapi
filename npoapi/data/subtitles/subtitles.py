from dataclasses import dataclass
from .subtitles_type import SubtitlesType

__NAMESPACE__ = "urn:vpro:media:subtitles:2009"


@dataclass
class Subtitles(SubtitlesType):
    class Meta:
        name = "subtitles"
        namespace = "urn:vpro:media:subtitles:2009"
