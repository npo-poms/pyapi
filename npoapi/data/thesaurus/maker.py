from dataclasses import dataclass
from .maker_type import MakerType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class Maker(MakerType):
    class Meta:
        name = "maker"
        namespace = "urn:vpro:gtaa:2017"
