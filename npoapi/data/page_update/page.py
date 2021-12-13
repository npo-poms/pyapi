from dataclasses import dataclass
from .page_update_type import PageUpdateType

__NAMESPACE__ = "urn:vpro:pages:update:2013"


@dataclass
class Page(PageUpdateType):
    class Meta:
        name = "page"
        namespace = "urn:vpro:pages:update:2013"
