from dataclasses import dataclass
from .name_type import NameType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Name(NameType):
    class Meta:
        name = "name"
        namespace = "urn:vpro:gtaa:2017"
