from dataclasses import dataclass
from .geographic_name_type import GeographicNameType

__NAMESPACE__ = "urn:vpro:gtaa:2017"


@dataclass
class GeographicName(GeographicNameType):
    class Meta:
        name = "geographicName"
        namespace = "urn:vpro:gtaa:2017"
