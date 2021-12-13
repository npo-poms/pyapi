from dataclasses import dataclass
from .group_update_type import GroupUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class Group(GroupUpdateType):
    class Meta:
        name = "group"
        namespace = "urn:vpro:media:update:2009"
