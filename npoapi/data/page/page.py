from dataclasses import dataclass
from .page_type import PageType

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass
class Page(PageType):
    class Meta:
        name = "page"
        namespace = "urn:vpro:pages:2013"
