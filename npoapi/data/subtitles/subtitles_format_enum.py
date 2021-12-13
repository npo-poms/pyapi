from enum import Enum

__NAMESPACE__ = "urn:vpro:media:subtitles:2009"


class SubtitlesFormatEnum(Enum):
    WEBVTT = "WEBVTT"
    TT888 = "TT888"
    EBU = "EBU"
    SRT = "SRT"
