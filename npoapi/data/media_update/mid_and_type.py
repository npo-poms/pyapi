from dataclasses import dataclass
from .mid_and_type_type import MidAndTypeType

__NAMESPACE__ = "urn:vpro:media:update:2009"


@dataclass
class MidAndType(MidAndTypeType):
    class Meta:
        name = "midAndType"
        namespace = "urn:vpro:media:update:2009"
