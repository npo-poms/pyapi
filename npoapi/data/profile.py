from dataclasses import dataclass, field
from typing import Optional
from npoapi.data.api_constraint_media import Filter

__NAMESPACE__ = "urn:vpro:api:profile:2013"


@dataclass
class ProfileDefinitionType:
    """
    :ivar filter:
    :ivar vpro_api_constraint_page_2013_filter:
    :ivar since:
    """
    class Meta:
        name = "profileDefinitionType"

    filter: Optional[Filter] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="urn:vpro:api:constraint:media:2013"
        )
    )
    vpro_api_constraint_page_2013_filter: Optional[Filter] = field(
        default=None,
        metadata=dict(
            name="filter",
            type="Element",
            namespace="urn:vpro:api:constraint:page:2013"
        )
    )
    since: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class ProfileType:
    """
    :ivar page_profile:
    :ivar media_profile:
    :ivar timestamp:
    :ivar name:
    """
    class Meta:
        name = "profileType"

    page_profile: Optional[ProfileDefinitionType] = field(
        default=None,
        metadata=dict(
            name="pageProfile",
            type="Element",
            namespace="urn:vpro:api:profile:2013"
        )
    )
    media_profile: Optional[ProfileDefinitionType] = field(
        default=None,
        metadata=dict(
            name="mediaProfile",
            type="Element",
            namespace="urn:vpro:api:profile:2013"
        )
    )
    timestamp: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
    name: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Profile(ProfileType):
    class Meta:
        name = "profile"
        namespace = "urn:vpro:api:profile:2013"
