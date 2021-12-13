from dataclasses import dataclass
from .media_list_result_type import MediaListResultType

__NAMESPACE__ = "urn:vpro:media:search:2012"


@dataclass
class ListType(MediaListResultType):
    class Meta:
        name = "list"
        namespace = "urn:vpro:media:search:2012"
