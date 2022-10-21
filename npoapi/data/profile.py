from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime
from npoapi.data.api_constraint_media import Filter as MediaFilter
from npoapi.data.api_constraint_page import Filter as PageFilter

__NAMESPACE__ = "urn:vpro:api:profile:2013"


@dataclass
class ProfileDefinitionType:
    class Meta:
        name = "profileDefinitionType"

    filter: Optional[MediaFilter] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:api:constraint:media:2013",
        }
    )
    vproApiConstraintPage2013Filter: Optional[PageFilter] = field(
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


@dataclass
class Profile(ProfileType):
    class Meta:
        name = "profile"
        namespace = "urn:vpro:api:profile:2013"
