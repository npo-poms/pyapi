from dataclasses import dataclass
from .profile_type import ProfileType

__NAMESPACE__ = "urn:vpro:api:profile:2013"


@dataclass
class Profile(ProfileType):
    class Meta:
        name = "profile"
        namespace = "urn:vpro:api:profile:2013"
