from dataclasses import dataclass
from .member_update_type import MemberUpdateType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class MemberUpdate(MemberUpdateType):
    class Meta:
        name = "memberUpdate"
        namespace = "urn:vpro:media:update:2009"
