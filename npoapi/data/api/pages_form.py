from dataclasses import dataclass
from .pages_form_type import PagesFormType

__NAMESPACE__ = "urn:vpro:api:2013"


@dataclass
class PagesForm(PagesFormType):
    class Meta:
        name = "pagesForm"
        namespace = "urn:vpro:api:2013"
