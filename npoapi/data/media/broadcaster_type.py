from dataclasses import dataclass
from .organization_type import OrganizationType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class BroadcasterType(OrganizationType):
    class Meta:
        name = "broadcasterType"
