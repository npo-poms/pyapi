from enum import Enum

__NAMESPACE__ = "urn:vpro:media:search:2012"


class MediaSortField(Enum):
    SORT_TITLE = "sortTitle"
    MID = "mid"
    TYPE = "type"
    MEDIA_TYPE = "mediaType"
    SORT_DATE = "sortDate"
    LAST_MODIFIED = "lastModified"
    CREATION_DATE = "creationDate"
    PUBLISH_STOP = "publishStop"
    PUBLISH_START = "publishStart"
    LAST_PUBLISHED = "lastPublished"
    LAST_MODIFIED_BY = "lastModifiedBy"
    CREATED_BY = "createdBy"
    LOCATIONS = "locations"
    MEMBEROF_COUNT = "memberofCount"
    EPISODEOF_COUNT = "episodeofCount"
