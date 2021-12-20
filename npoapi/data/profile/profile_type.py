from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from .profile_definition_type import ProfileDefinitionType

__NAMESPACE__ = "urn:vpro:api:profile:2013"


@dataclass
class ProfileType:
    class Meta:
        name = "profileType"

    pageProfile: Optional[ProfileDefinitionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:profile:2013",
        }
    )
    mediaProfile: Optional[ProfileDefinitionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:profile:2013",
        }
    )
    timestamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
