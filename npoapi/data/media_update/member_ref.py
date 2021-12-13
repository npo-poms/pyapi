from dataclasses import dataclass
from .member_ref_update_type import MemberRefUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class MemberRef(MemberRefUpdateType):
    class Meta:
        name = "memberRef"
        namespace = "urn:vpro:media:update:2009"
