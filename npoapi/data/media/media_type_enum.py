from enum import Enum

__NAMESPACE__ = "urn:vpro:media:2009"


class MediaTypeEnum(Enum):
    """
    :cvar MEDIA: The abstract type denoting every possible media type
    :cvar GROUP: The abstract type denoting every possible group type
    :cvar PROGRAM: The abstract type denoting every possible program type
    :cvar SEGMENTTYPE: The abstract type denoting every possible segment type
    :cvar STRAND:
    :cvar ALBUM:
    :cvar PLAYLIST:
    :cvar ARCHIVE:
    :cvar SEASON:
    :cvar SERIES:
    :cvar UMBRELLA:
    :cvar BROADCAST:
    :cvar MOVIE:
    :cvar TRAILER:
    :cvar CLIP:
    :cvar TRACK:
    :cvar SEGMENT:
    :cvar VISUALRADIO:
    :cvar VISUALRADIOSEGMENT:
    :cvar PROMO:
    :cvar RECORDING:
    :cvar COLLECTION:
    """
    MEDIA = "MEDIA"
    GROUP = "GROUP"
    PROGRAM = "PROGRAM"
    SEGMENTTYPE = "SEGMENTTYPE"
    STRAND = "STRAND"
    ALBUM = "ALBUM"
    PLAYLIST = "PLAYLIST"
    ARCHIVE = "ARCHIVE"
    SEASON = "SEASON"
    SERIES = "SERIES"
    UMBRELLA = "UMBRELLA"
    BROADCAST = "BROADCAST"
    MOVIE = "MOVIE"
    TRAILER = "TRAILER"
    CLIP = "CLIP"
    TRACK = "TRACK"
    SEGMENT = "SEGMENT"
    VISUALRADIO = "VISUALRADIO"
    VISUALRADIOSEGMENT = "VISUALRADIOSEGMENT"
    PROMO = "PROMO"
    RECORDING = "RECORDING"
    COLLECTION = "COLLECTION"
