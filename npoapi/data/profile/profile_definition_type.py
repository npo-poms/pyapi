from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from ..api_constraint_media.filter import Filter
from ..api_constraint_page.filter import Filter as FilterFilter

__NAMESPACE__ = "urn:vpro:api:profile:2013"


@dataclass
class ProfileDefinitionType:
    class Meta:
        name = "profileDefinitionType"

    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    vpro_api_constraint_page_2013_filter: Optional[FilterFilter] = field(
        default=None,
        metadata={
            "name": "filter",
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:page:2013",
        }
    )
    since: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
