from dataclasses import dataclass
from .change_type import ChangeType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class Change(ChangeType):
    class Meta:
        name = "change"
        namespace = "urn:vpro:api:2013"
